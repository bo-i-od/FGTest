#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
穷举 3..8 × 3..8 牌面 + 宝物(旋转允许) 的题面，并输出填充率。
两种模式：
- 面积模式：只按面积筛选、尺寸能入（不验证实际摆放）
- 精确模式：验证是否能在棋盘内不重叠摆放（回溯+位板）

输出 CSV: board_h,board_w,total_area,board_area,fill_rate,pieces
pieces 字段只列非零的宝物数量，如: "1x2=2;1x3=1;3x3=1"
"""

from dataclasses import dataclass
from functools import lru_cache
import argparse
import csv
from typing import List, Tuple, Dict, Iterable

@dataclass(frozen=True)
class PieceType:
    name: str
    h: int
    w: int

    @property
    def area(self) -> int:
        return self.h * self.w

# 题目给定的宝物（矩形，允许旋转）
PIECES: Tuple[PieceType, ...] = (
    # PieceType("1x2", 1, 1),
    PieceType("1x2", 1, 2),
    PieceType("1x3", 1, 3),
    PieceType("1x4", 1, 4),
    # PieceType("1x5", 1, 5),
    PieceType("2x2", 2, 2),
    PieceType("2x3", 2, 3),
    PieceType("2x4", 2, 4),
    PieceType("3x3", 3, 3),
    PieceType("3x4", 3, 4),
    PieceType("4x4", 4, 4),
)

def orientations(p: PieceType) -> List[Tuple[int, int]]:
    """返回去重后的(高,宽)方向列表"""
    if p.h == p.w:
        return [(p.h, p.w)]
    return [(p.h, p.w), (p.w, p.h)]

def fits_board(H: int, W: int, p: PieceType) -> bool:
    """是否至少有一个方向能放进 H×W"""
    return any(h <= H and w <= W for h, w in orientations(p))

def capacity_upper_bound(H: int, W: int, p: PieceType) -> int:
    """
    给定单一宝物类型 p，在 H×W 内“理论”上限数量的一个安全上界（用于枚举剪枝）。
    使用：面积上界 + 两种朝向的格点容量和（松上界）。
    """
    A = H * W
    caps = 0
    for h, w in orientations(p):
        if h <= H and w <= W:
            caps += (H // h) * (W // w)
    return min(A // p.area, caps)

def enumerate_count_vectors(H: int, W: int,
                            min_fill: float,
                            max_fill: float,
                            max_pieces: int = None) -> Iterable[Tuple[List[int], int]]:
    """
    枚举每种宝物的数量向量 counts（列表与 PIECES 对应），使得：
    - 面积和 <= H*W
    - 填充率在 [min_fill, max_fill]
    - 单个宝物至少要能放进牌面（否则该宝物数量强制为0）
    返回 (counts, total_area)
    注意：这里只做面积与尺寸的快速筛选，不验证是否能真实摆放。
    """
    A = H * W
    n = len(PIECES)
    # 针对每种宝物给出数量上界
    caps = [capacity_upper_bound(H, W, p) if fits_board(H, W, p) else 0 for p in PIECES]
    areas = [p.area for p in PIECES]

    # 用于填充率剪枝的“剩余最大面积”
    suffix_max_area = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_max_area[i] = suffix_max_area[i + 1] + caps[i] * areas[i]

    counts = [0] * n
    results = []

    def dfs(i: int, used_area: int, used_cnt: int):
        # 填充率剪枝（上界/下界）
        if used_area > int(max_fill * A + 1e-9):
            return
        # 即使把后面的都加满，仍达不到 min_fill，也剪枝
        if used_area + suffix_max_area[i] < int(min_fill * A - 1e-9):
            return

        if i == n:
            if used_area == 0:
                return  # 至少要有一个宝物
            fill_ok = (min_fill - 1e-12) <= (used_area / A) <= (max_fill + 1e-12)
            if fill_ok:
                results.append((counts.copy(), used_area))
            return

        area_i = areas[i]
        cap_i = caps[i]
        if max_pieces is not None:
            cap_i = min(cap_i, max_pieces - used_cnt)

        # 循环数量
        # 小优化：不必尝试超过面积上限的数量
        if area_i > 0:
            cap_i = min(cap_i, (A - used_area) // area_i)

        for c in range(cap_i + 1):
            counts[i] = c
            dfs(i + 1, used_area + c * area_i, used_cnt + c)
        counts[i] = 0

    dfs(0, 0, 0)
    return results

def precompute_placements(H: int, W: int) -> Tuple[List[List[int]], int]:
    """
    为每种宝物预计算所有摆放位置（位板），以及每个格子 -> 可覆盖它的摆放列表。
    返回:
      cover_per_piece: 长度为 len(PIECES) 的列表，
                       cover_per_piece[i] 是长度 H*W 的列表，
                       其中每个元素是能覆盖该格子 e 的摆放掩码列表。
      full_mask: 棋盘满掩码
    """
    cell_count = H * W
    full_mask = (1 << cell_count) - 1
    cover_per_piece: List[List[List[int]]] = []

    def rect_mask(r0: int, c0: int, h: int, w: int) -> int:
        m = 0
        for dr in range(h):
            base = (r0 + dr) * W + c0
            for dc in range(w):
                m |= 1 << (base + dc)
        return m

    for p in PIECES:
        cover_map = [[] for _ in range(cell_count)]
        orients = orientations(p)
        # 去除等价方向的重复（若 h==w 已去重）
        seen = set(orients)
        for (ph, pw) in seen:
            if ph > H or pw > W:
                continue
            for r in range(H - ph + 1):
                for c in range(W - pw + 1):
                    m = rect_mask(r, c, ph, pw)
                    mm = m
                    while mm:
                        lowbit = mm & -mm
                        idx = (lowbit.bit_length() - 1)
                        cover_map[idx].append(m)
                        mm &= mm - 1
        cover_per_piece.append(cover_map)
    return cover_per_piece, full_mask

def is_placeable(H: int, W: int, counts: List[int],
                 precomp: Tuple[List[List[int]], int]) -> bool:
    """
    精确模式：验证给定 counts 是否能在 H×W 内不重叠摆下。
    回溯 + “首个空格覆盖”策略 + 位板。
    """
    if sum(counts) == 0:
        return False
    cover_per_piece, full_mask = precomp
    # 若某宝物根本放不进去，则直接失败
    for i, c in enumerate(counts):
        if c > 0 and not fits_board(H, W, PIECES[i]):
            return False

    # 为了减枝，按面积降序访问宝物类型
    order = sorted(range(len(PIECES)), key=lambda i: PIECES[i].area, reverse=True)
    counts_ord = tuple(counts[i] for i in order)
    cover_ord = [cover_per_piece[i] for i in order]

    @lru_cache(maxsize=None)
    def dfs(board_mask: int, counts_state: Tuple[int, ...]) -> bool:
        if sum(counts_state) == 0:
            return True
        empties = full_mask & ~board_mask
        if empties == 0:
            return False
        # 选取最靠前的空位（最低位的1）
        e_lowbit = (empties & -empties)
        e = e_lowbit.bit_length() - 1

        # 尝试用每种还有剩余的宝物覆盖该格子
        for i, cnt in enumerate(counts_state):
            if cnt == 0:
                continue
            # 仅能用覆盖 e 的摆放
            for place_mask in cover_ord[i][e]:
                if (place_mask & board_mask) != 0:
                    continue
                # 放下这个宝物
                new_counts = list(counts_state)
                new_counts[i] -= 1
                if dfs(board_mask | place_mask, tuple(new_counts)):
                    return True
        return False

    return dfs(0, counts_ord)

def write_results_csv(path: str,
                      rows: Iterable[Tuple[int, int, int, int, float, str]]):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["board_h", "board_w", "total_area",
                         "board_area", "fill_rate", "pieces"])
        for row in rows:
            writer.writerow(row)

def format_pieces(counts: List[int]) -> str:
    parts = []
    for p, c in zip(PIECES, counts):
        if c > 0:
            parts.append(f"{p.name}={c}")
    return ";".join(parts) if parts else ""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-h", type=int, default=5)
    parser.add_argument("--max-h", type=int, default=7)
    parser.add_argument("--min-w", type=int, default=6)
    parser.add_argument("--max-w", type=int, default=7)
    parser.add_argument("--min-fill", type=float, default=0.3)
    parser.add_argument("--max-fill", type=float, default=0.7)
    parser.add_argument("--max-pieces", type=int, default=6,
                        help="可选：限制总宝物个数上限，以加速枚举")
    parser.add_argument("--out", type=str, default="results.csv")
    args = parser.parse_args()

    rows = []
    total_boards = 0
    for H in range(args.min_h, args.max_h + 1):
        for W in range(args.min_w, args.max_w + 1):
            total_boards += 1
            if H > W:
                continue
            if W-H > 2:
                continue
            A = H * W
            # 面积模式先枚举所有候选 count 向量
            candidates = enumerate_count_vectors(
                H, W, args.min_fill, args.max_fill, args.max_pieces
            )
            # 精确模式预计算摆放
            precomp = precompute_placements(H, W)

            for counts, total_area in candidates:
                if not is_placeable(H, W, counts, precomp):
                    continue
                fill_rate = total_area / A

                # # 填充率限制
                # if fill_rate > 0.7 * 0.01 * (100 - total_area):
                #     continue
                # if fill_rate < 0.3 * 0.01 * (100 - total_area):
                #     continue
                odd = 0
                for count in counts:
                    if count % 2 != 0:
                        odd += 1
                if odd > 2:
                    continue
                if counts[0] % 2 != 0:
                    continue
                rows.append((
                    H, W, total_area, A, round(fill_rate, 6),
                    format_pieces(counts)
                ))
    res = {}
    cur = 0
    while cur < len(rows):
        row = rows[cur]
        k = f"{row[0]}_{row[1]}"
        if k not in res:
            res[k] = 1
            cur += 1
            continue
        res[k] += 1
        cur += 1
    rows_write = []
    cur = 0
    while cur < len(rows):
        row = rows[cur]
        k = f"{row[0]}_{row[1]}"
        interval = int(res[k] / 25 + 1)
        if cur % interval != 0:
            cur += 1
            continue
        rows_write.append(row)
        cur += 1
    write_results_csv(args.out, rows_write)
    print(f"完成：{len(rows_write)} 行写入 {args.out}。枚举的牌面数={total_boards}。")
    # write_results_csv(args.out, rows)
    # print(f"完成：{len(rows)} 行写入 {args.out}。枚举的牌面数={total_boards}。")

if __name__ == "__main__":
    main()