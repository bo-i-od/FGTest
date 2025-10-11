# file: placement_solver.py
from __future__ import annotations
from typing import Dict, List, Tuple
from functools import lru_cache, wraps
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed
from itertools import permutations
import multiprocessing, json, os, math, time, sys
from tqdm import tqdm


###############################################################################
#                           多进程 Wrapper 函数                              #
###############################################################################
def _evaluate_task_wrapper(args):
    """
    顶层 helper，使得 multiprocessing 可 pickle。
    """
    solver, assignment, locked, forbids, cand_indices, pos, U = args
    return solver._evaluate(assignment, locked, forbids, cand_indices, pos, U)


###############################################################################
#                               通用工具 / 缓存                               #
###############################################################################
CACHE_FILE = "ep_cache.json"


def _hist_key(hist: dict, policy: str) -> str:
    return policy + "|" + ";".join(f"{k}:{hist[k]}" for k in sorted(hist))


def _load_cache() -> dict:
    return json.load(open(CACHE_FILE, "r")) if os.path.exists(CACHE_FILE) else {}


def _save_cache(c: dict):
    json.dump(c, open(CACHE_FILE, "w"), indent=2, sort_keys=True)


def disk_cached(fn):
    cache = _load_cache()

    @wraps(fn)
    def wrapper(hist, policy="optimal"):
        key = _hist_key(hist, policy)
        if key in cache:
            return cache[key]
        val = fn(hist, policy)
        cache[key] = val
        _save_cache(cache)
        return val

    return wrapper


###############################################################################
#                       直方图 → 颜色计数 以及 secret 生成                     #
###############################################################################
def histogram_to_counts(hist: Dict[int, int]) -> List[int]:
    out = []
    for size, num in sorted(hist.items()):      # 保证顺序稳定
        out.extend([size] * num)
    return out                                  # e.g. {1:7} → [1,1,1,1,1,1,1]


def gen_all_secrets(counts: List[int]) -> List[Tuple[int, ...]]:
    """
    返回所有满足颜色计数要求的排列（去重）。
    例如 counts=[1,1] → [(0,1),(1,0)]
    """
    T = sum(counts)
    if T == 0:
        return []
    colors = []
    for c, cnt in enumerate(counts):
        colors.extend([c] * cnt)                # [0,1,1,2,2,2 ...]
    perms = set(permutations(colors, T))        # 小规模去重
    return list(perms)


###############################################################################
#                     工具：生成所有直方图（可批量测试用）                    #
###############################################################################
def generate_partitions(n: int):
    """整数分拆。"""
    def helper(m, max_v):
        if m == 0:
            yield []
            return
        for i in range(min(m, max_v), 0, -1):
            for tail in helper(m - i, i):
                yield [i] + tail
    yield from helper(n, n)


def generate_all_histograms(min_balls=3, max_balls=7):
    all_hist = []
    for tot in range(min_balls, max_balls + 1):
        for part in generate_partitions(tot):
            h = {}
            for x in part:
                h[x] = h.get(x, 0) + 1
            all_hist.append(h)
    return all_hist


###############################################################################
#                                核心求解类                                   #
###############################################################################
_big_penalty = 10 ** 9          # assignments==[] 时的“有限大”惩罚


class ExpectationSolver:
    def __init__(self, hist: Dict[int, int], policy="optimal"):
        assert policy in ("optimal", "uniform")
        self.policy = policy
        self.counts = histogram_to_counts(hist)
        self.K = len(self.counts)               # 颜色种类
        self.T = sum(self.counts)               # 球总数

        if self.T == 0:
            self.all_secrets = []
        else:
            print("Generating secrets ...")
            t0 = time.time()
            self.all_secrets = gen_all_secrets(self.counts)
            print(f"  {len(self.all_secrets)} secrets generated "
                  f"in {time.time()-t0:.2f}s")

    # ----------------------------------------------------------------- #
    #                           状态辅助函数                            #
    # ----------------------------------------------------------------- #
    @lru_cache(maxsize=None)
    def _candidate_indices(self,
                           locked: Tuple[int, ...],
                           forbids: Tuple[int, ...]) -> Tuple[int, ...]:
        res = []
        for idx, s in enumerate(self.all_secrets):
            ok = True
            for i in range(self.T):
                if locked[i] != -1 and s[i] != locked[i]:
                    ok = False
                    break
                if (forbids[i] >> s[i]) & 1:
                    ok = False
                    break
            if ok:
                res.append(idx)
        return tuple(res)

    def _remaining_counts(self, locked: Tuple[int, ...]) -> List[int]:
        rem = self.counts[:]
        for c in locked:
            if c != -1:
                rem[c] -= 1
        return rem

    # ---------- 生成 assignment；做一个很粗的对称剪枝 ---------- #
    def _gen_assignments(self,
                         locked: Tuple[int, ...],
                         forbids: Tuple[int, ...]) -> List[Tuple[int, ...]]:
        rem = self._remaining_counts(locked)
        pos = [i for i in range(self.T) if locked[i] == -1]
        A = [-1] * self.T
        out = []

        def dfs(k: int):
            if k == len(pos):
                out.append(tuple(A))
                return
            i = pos[k]
            for c in range(self.K):
                if rem[c] == 0 or ((forbids[i] >> c) & 1):
                    continue
                A[i] = c
                rem[c] -= 1
                dfs(k + 1)
                rem[c] += 1
                A[i] = -1

        dfs(0)

        # 如果所有剩余颜色计数 ≤1，置换等价，只留首个
        if all(r <= 1 for r in self._remaining_counts(locked)):
            out = out[:1]
        return out

    # --------- 评估单个 assignment（可在子进程运行） --------- #
    def _evaluate(self,
                  assignment: Tuple[int, ...],
                  locked: Tuple[int, ...],
                  forbids: Tuple[int, ...],
                  cand_indices: Tuple[int, ...],
                  pos: Tuple[int, ...],
                  U: int) -> float:
        counts_by_mask = defaultdict(int)
        for idx in cand_indices:
            sec = self.all_secrets[idx]
            mask = 0
            for i in pos:
                if sec[i] == assignment[i]:
                    mask |= 1 << i
            counts_by_mask[mask] += 1

        total = len(cand_indices)
        exp_future = 0.0
        for mask, cnt in counts_by_mask.items():
            new_locked = list(locked)
            new_forbids = list(forbids)
            for i in pos:
                if (mask >> i) & 1:          # 命中
                    new_locked[i] = assignment[i]
                else:                        # 未命中
                    new_forbids[i] |= 1 << assignment[i]
            future = self.expected_cost(tuple(new_locked),
                                        tuple(new_forbids),
                                        depth=1)
            exp_future += cnt / total * future
        return U + exp_future

    # ---------------------------- 主递归 ---------------------------- #
    @lru_cache(maxsize=None)
    def expected_cost(self,
                      locked: Tuple[int, ...],
                      forbids: Tuple[int, ...],
                      depth: int = 0) -> float:

        # 基本完结态
        if all(x != -1 for x in locked):
            return 0.0

        pos = tuple(i for i in range(self.T) if locked[i] == -1)
        U = len(pos)

        cand_indices = self._candidate_indices(locked, forbids)
        if not cand_indices:
            return 0.0                     # 理论上不会发生

        assignments = self._gen_assignments(locked, forbids)
        if not assignments:
            return _big_penalty

        # ---------------- 顶层：并行 + 剪枝 ----------------
        if depth == 0:
            tasks = [(self, a, locked, forbids, cand_indices, pos, U)
                     for a in assignments]
            max_workers = min(multiprocessing.cpu_count() - 2, len(assignments))
            # -------- uniform 策略：所有 assignment 取均值 --------
            if self.policy == "uniform":

                with ProcessPoolExecutor(max_workers=max_workers) as pool:
                    vals = list(tqdm(pool.map(_evaluate_task_wrapper, tasks),
                                     total=len(assignments),
                                     desc="uniform/parallel"))
                return sum(vals) / len(vals)

            # -------- optimal 策略：取最小值，带剪枝 --------
            best = math.inf
            with ProcessPoolExecutor(max_workers=max_workers) as pool:
                futs = {pool.submit(_evaluate_task_wrapper, t): t[1]
                        for t in tasks}

                for fut in tqdm(as_completed(futs),
                                total=len(futs),
                                desc="optimal/parallel"):
                    v = fut.result()
                    if v < best:
                        best = v
                        if best <= U:        # 已达理论下界 → 早停
                            # 取消剩余任务（仅限尚未开始的）
                            for f in futs:
                                f.cancel()
                            break
            return best

        # ------------- 非顶层：串行 + 剪枝（同上版本） -------------
        if self.policy == "uniform":
            vals = [self._evaluate(a, locked, forbids, cand_indices, pos, U)
                    for a in assignments]
            return sum(vals) / len(vals)
        best = math.inf
        for a in assignments:
            v = self._evaluate(a, locked, forbids, cand_indices, pos, U)
            if v < best:
                best = v
                if best <= U:
                    break
        return best


###############################################################################
#                           对外接口（带磁盘缓存）                             #
###############################################################################
@disk_cached
def expected_placements(hist: Dict[int, int], policy="optimal") -> float:
    if not hist:
        return 0.0
    print("=" * 60)
    print(f"Start histogram={hist}, policy='{policy}'")
    solver = ExpectationSolver(hist, policy)
    if solver.T == 0:
        return 0.0
    locked0 = tuple([-1] * solver.T)
    forbids0 = tuple([0] * solver.T)
    ans = solver.expected_cost(locked0, forbids0, depth=0)
    print(f"Finished.  Expected placements = {ans:.6f}")
    print("=" * 60)
    return ans


###############################################################################
#                                   Demo                                      #
###############################################################################
def main():
    # demo：批量跑 3~6 个球的所有直方图
    all_hists = generate_all_histograms(min_balls=3, max_balls=7)

    for hist in all_hists:
        v_opt = expected_placements(hist, 'optimal')
        v_uni = expected_placements(hist, 'uniform')
        if abs(v_opt - v_uni) > 0.5:
            raise RuntimeError(f"Inconsistent: {hist}")
        print(f"{hist}  ->  optimal={v_opt:.3f} , uniform={v_uni:.3f}")


if __name__ == "__main__":
    multiprocessing.freeze_support()  # Windows 兼容
    main()