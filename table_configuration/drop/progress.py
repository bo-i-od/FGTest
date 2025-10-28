import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import sys
import os
from datetime import datetime

#  48160. [279, 140, 70, 35, 18, 9, 6, 2, 1]
#  48161. [279, 140, 70, 35, 18, 10, 4, 3, 1]
#  48176. [279, 140, 70, 36, 17, 9, 5, 3, 1]
# [140, 70, 35, 18, 7, 5, 3, 1, 1]

class SolutionWriter:
    """
    线程安全的解写入器，直接写入文件防止内存爆炸
    """

    def __init__(self, filename, x, n, method_name=""):
        self.filename = filename
        self.x = x
        self.n = n
        self.method_name = method_name
        self.lock = threading.Lock()
        self.solution_count = 0
        self.file_handle = None
        self._write_header()

    def _write_header(self):
        """写入文件头"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write("组合优化问题解集 (流式输出)\n")
            f.write("=" * 60 + "\n")
            f.write(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"问题参数: x = {self.x}, n = {self.n}\n")
            f.write(f"求解方法: {self.method_name}\n")
            f.write(f"约束条件:\n")
            f.write(f"  - Σ(a_i) = {self.n}\n")
            f.write(f"  - Σ(i * a_i) = {self.n} (i=1 to {self.x - 1})\n")
            f.write(f"  - a_0 ≥ a_1 ≥ ... ≥ a_{self.x - 1} ≥ 1\n")
            f.write(f"  - a_i ≤ max((0.5)^(i+1) * {self.n}, 1) for i = 0, 1, 2 (仅前三个变量)\n")
            f.write("=" * 60 + "\n\n")
            f.write("所有解:\n")
            f.write("-" * 40 + "\n")

    def write_solution(self, solution):
        """线程安全地写入一个解"""
        with self.lock:
            self.solution_count += 1
            with open(self.filename, 'a', encoding='utf-8') as f:
                f.write(f"{self.solution_count:6d}. {solution}\n")

                if self.solution_count % 1000 == 0:
                    f.write(f"     ... (已找到 {self.solution_count} 个解)\n\n")

    def write_footer(self):
        """写入文件尾部统计信息"""
        with self.lock:
            with open(self.filename, 'a', encoding='utf-8') as f:
                f.write(f"\n" + "=" * 60 + "\n")
                f.write("最终统计:\n")
                f.write("-" * 40 + "\n")
                f.write(f"总解数: {self.solution_count}\n")
                f.write(f"完成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    def get_count(self):
        """获取当前解的数量"""
        with self.lock:
            return self.solution_count


def get_max_value_constraint(i, n):
    """
    计算第i个变量的最大值约束: max((0.5)^(i+1) * n, 1)
    只对 i = 0, 1, 2 生效，其他返回无穷大
    """
    if i <= 2:
        return max(int((0.5 ** (i + 1)) * n), 1)
    else:
        return float('inf')  # 对于i>=3的变量，没有额外约束


def check_feasibility(x, n):
    """
    检查问题的可行性
    """
    min_weighted = x * (x - 1) // 2

    print(f"🔍 可行性分析:")
    print(f"   最小加权和: {min_weighted}")
    print(f"   目标和: {n}")

    # 显示约束（只对前三个变量）
    constraints_info = []
    for i in range(min(3, x)):
        max_val = get_max_value_constraint(i, n)
        constraints_info.append(f'a{i}≤{max_val}')

    if x > 3:
        constraints_info.append(f'a3...a{x - 1}无额外约束')

    print(f"   约束: {constraints_info}")

    if n < min_weighted:
        print(f"❌ 不可行: n={n} < 最小加权和 {min_weighted}")
        return False

    print(f"✅ 初步可行性检查通过")
    return True


def find_all_solutions_with_constraints_single_thread(x, n, writer, a0_range=None, show_progress=True):
    """
    带新约束条件的单线程求解器，直接写入文件
    """
    if not check_feasibility(x, n):
        return 0

    # 计算a0的范围（只对a0应用约束）
    max_a0_constraint = get_max_value_constraint(0, n)
    max_a0 = min(n - (x - 1), max_a0_constraint)
    min_a0 = 1

    if a0_range:
        min_a0, max_a0 = a0_range
        max_a0 = min(max_a0, max_a0_constraint)

    if max_a0 < min_a0:
        print(f"⚠️  a0范围无效: [{min_a0}, {max_a0}]")
        return 0

    total_a0_count = max_a0 - min_a0 + 1
    processed_a0 = 0
    last_progress_time = time.time()
    local_solution_count = 0

    def backtrack(index, current, last_val, remaining_sum, remaining_weighted):
        nonlocal processed_a0, last_progress_time, local_solution_count

        if index == x:
            if remaining_sum == 0 and remaining_weighted == 0:
                writer.write_solution(current[:])
                local_solution_count += 1
            return

        # 进度显示
        if index == 0 and show_progress:
            current_time = time.time()
            if current_time - last_progress_time > 2:
                progress = (processed_a0 / total_a0_count) * 100
                total_found = writer.get_count()
                print(f"📈 进度: {progress:.1f}% ({processed_a0}/{total_a0_count}), 已找到 {total_found} 个解",
                      end='\r')
                sys.stdout.flush()
                last_progress_time = current_time

        # 应用约束
        low = 1
        high = min(last_val, remaining_sum)

        # 只对前三个变量应用额外约束
        if index <= 2:
            constraint_max = get_max_value_constraint(index, n)
            high = min(high, constraint_max)

        if index == 0 and a0_range:
            low = max(low, a0_range[0])
            high = min(high, a0_range[1])

        # 剪枝检查
        remaining_positions = x - index
        min_possible_weighted = sum(j for j in range(max(1, index), x))
        max_possible_weighted = sum(j * high for j in range(max(1, index), x))

        if remaining_weighted < min_possible_weighted or remaining_weighted > max_possible_weighted:
            return

        for val in range(low, high + 1):
            new_remaining_sum = remaining_sum - val
            weight = index if index >= 1 else 0
            new_remaining_weighted = remaining_weighted - weight * val

            if new_remaining_sum < 0 or new_remaining_weighted < 0:
                continue

            current.append(val)

            if index == 0:
                processed_a0 = val - min_a0 + 1

            backtrack(index + 1, current, val, new_remaining_sum, new_remaining_weighted)
            current.pop()

    backtrack(0, [], float('inf'), n, n)

    if show_progress:
        print(" " * 80, end='\r')
        sys.stdout.flush()

    return local_solution_count


def find_all_solutions_with_constraints_multithread(x, n, num_threads=None):
    """
    带约束的多线程版本，直接写入文件
    """
    if num_threads is None:
        num_threads = min(8, threading.active_count() + 4)

    if not check_feasibility(x, n):
        return 0

    # 创建输出文件
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"solutions_constrained_x{x}_n{n}_{timestamp}.txt"
    writer = SolutionWriter(filename, x, n, "带约束多线程")

    max_a0_constraint = get_max_value_constraint(0, n)
    max_a0 = min(n - (x - 1), max_a0_constraint)
    min_a0 = 1

    if max_a0 < min_a0:
        print(f"❌ a0范围无效: [{min_a0}, {max_a0}]")
        writer.write_footer()
        return 0

    print(f"🚀 使用 {num_threads} 个线程，a0 范围: [{min_a0}, {max_a0}]")
    print(f"📁 解将直接写入文件: {filename}")

    # 分割a0范围
    a0_ranges = []
    range_size = max(1, (max_a0 - min_a0 + 1) // num_threads)

    for i in range(num_threads):
        start = min_a0 + i * range_size
        if i == num_threads - 1:
            end = max_a0
        else:
            end = min(max_a0, min_a0 + (i + 1) * range_size - 1)

        if start <= max_a0:
            a0_ranges.append((start, end))

    completed_threads = 0
    thread_lock = threading.Lock()
    start_time = time.time()

    def progress_callback(future):
        nonlocal completed_threads
        with thread_lock:
            completed_threads += 1
            local_count = future.result()
            current_time = time.time()
            elapsed = current_time - start_time

            total_solutions = writer.get_count()
            print(f"✅ 线程 {completed_threads}/{len(a0_ranges)} 完成，本线程找到 {local_count} 个解")
            print(
                f"📈 总进度: {(completed_threads / len(a0_ranges)) * 100:.1f}%, 总解数: {total_solutions} (耗时: {elapsed:.1f}s)")

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for i, a0_range in enumerate(a0_ranges):
            print(f"🎯 启动线程 {i + 1}: 处理 a0 ∈ [{a0_range[0]}, {a0_range[1]}]")
            future = executor.submit(find_all_solutions_with_constraints_single_thread, x, n, writer, a0_range, False)
            future.add_done_callback(progress_callback)
            futures.append(future)

        for future in as_completed(futures):
            pass

    end_time = time.time()
    total_solutions = writer.get_count()
    writer.write_footer()

    print(f"✅ 求解完成!")
    elapsed_time = end_time - start_time
    print(f"⏱️  总耗时: {elapsed_time:.2f} 秒")
    print(f"🎯 总解数: {total_solutions}")
    print(f"📁 解已保存到: {filename}")

    if os.path.exists(filename):
        print(f"📊 文件大小: {os.path.getsize(filename) / 1024:.1f} KB")

    if elapsed_time > 0:
        print(f"🎯 求解速度: {total_solutions / elapsed_time:.1f} 解/秒")
    else:
        print(f"🎯 求解速度: 极快 (耗时 < 0.01秒)")

    return total_solutions


def find_all_solutions_with_constraints_advanced_multithread(x, n, num_threads=None):
    """
    带约束的高级多线程版本，通过前两层分割任务
    """
    if num_threads is None:
        num_threads = min(8, threading.active_count() + 4)

    if not check_feasibility(x, n):
        return 0

    # 创建输出文件
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"solutions_constrained_adv_x{x}_n{n}_{timestamp}.txt"
    writer = SolutionWriter(filename, x, n, "带约束高级多线程")

    print("🔄 生成任务...")
    task_generation_start = time.time()

    tasks = []
    max_a0_constraint = get_max_value_constraint(0, n)
    max_a0 = min(n - (x - 1), max_a0_constraint)

    print(f"🔍 调试信息: max_a0 = {max_a0}, 约束值 = {max_a0_constraint}")

    for a0 in range(1, max_a0 + 1):
        remaining_sum_after_a0 = n - a0
        remaining_weighted_after_a0 = n  # a0的权重为0

        if remaining_sum_after_a0 < x - 1:  # 剩余位置至少需要x-1个1
            continue

        # a1的约束
        max_a1_constraint = get_max_value_constraint(1, n) if x > 1 else float('inf')
        max_a1 = min(a0, remaining_sum_after_a0, max_a1_constraint)

        for a1 in range(1, max_a1 + 1):
            remaining_sum = remaining_sum_after_a0 - a1
            remaining_weighted = remaining_weighted_after_a0 - a1  # a1的权重为1

            if remaining_sum < 0 or remaining_weighted < 0:
                continue

            remaining_positions = x - 2
            if remaining_positions > 0:
                # 更宽松的检查，因为后面的变量没有额外约束
                min_remaining_sum = remaining_positions  # 每个位置至少1
                max_remaining_sum = remaining_positions * a1  # 每个位置最多a1（递减约束）

                if remaining_sum < min_remaining_sum or remaining_sum > max_remaining_sum:
                    continue

                # 加权和检查
                min_remaining_weighted = sum(i for i in range(2, x))  # 每个位置至少1
                max_remaining_weighted = sum(i * a1 for i in range(2, x))  # 后面变量无额外约束

                if remaining_weighted < min_remaining_weighted or remaining_weighted > max_remaining_weighted:
                    continue
            elif remaining_positions == 0:
                # x=2的情况
                if remaining_sum != 0 or remaining_weighted != 0:
                    continue

            tasks.append((a0, a1, remaining_sum, remaining_weighted))

    task_generation_time = time.time() - task_generation_start
    print(f"✅ 任务生成完成: {len(tasks)} 个任务 (耗时: {task_generation_time:.2f}s)")

    if len(tasks) == 0:
        print("❌ 没有生成任何任务")
        writer.write_footer()
        return 0

    print(f"📁 解将直接写入文件: {filename}")

    def solve_subtask_with_constraints(task):
        a0, a1, remaining_sum, remaining_weighted = task
        local_count = 0

        def backtrack_constrained(index, current, last_val, rem_sum, rem_weighted):
            nonlocal local_count

            if index == x:
                if rem_sum == 0 and rem_weighted == 0:
                    writer.write_solution(current[:])
                    local_count += 1
                return

            remaining_positions = x - index
            min_val = max(1, rem_sum - (remaining_positions - 1) * last_val)
            max_val = min(last_val, rem_sum)

            # 只对前三个变量应用额外约束
            if index <= 2:
                constraint_max = get_max_value_constraint(index, n)
                max_val = min(max_val, constraint_max)

            if min_val > max_val:
                return

            # 剪枝检查
            min_possible_weighted = sum(j for j in range(max(1, index), x))
            max_possible_weighted = sum(j * max_val for j in range(max(1, index), x))

            if rem_weighted < min_possible_weighted or rem_weighted > max_possible_weighted:
                return

            for val in range(min_val, max_val + 1):
                new_rem_sum = rem_sum - val
                weight = index if index >= 1 else 0
                new_rem_weighted = rem_weighted - weight * val

                if new_rem_sum >= 0 and new_rem_weighted >= 0:
                    current.append(val)
                    backtrack_constrained(index + 1, current, val, new_rem_sum, new_rem_weighted)
                    current.pop()

        if x <= 2:
            if x == 2 and remaining_sum == 0 and remaining_weighted == 0:
                writer.write_solution([a0, a1])
                local_count += 1
        else:
            backtrack_constrained(2, [a0, a1], a1, remaining_sum, remaining_weighted)

        return local_count

    # 执行任务
    start_time = time.time()
    last_progress_time = start_time
    completed = 0
    total_tasks = len(tasks)

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        future_to_task = {executor.submit(solve_subtask_with_constraints, task): task for task in tasks}

        for future in as_completed(future_to_task):
            local_count = future.result()
            completed += 1

            current_time = time.time()
            if current_time - last_progress_time > 1 or completed % max(1, total_tasks // 50) == 0:
                progress = (completed / total_tasks) * 100
                elapsed = current_time - start_time
                total_solutions = writer.get_count()

                if completed > 0 and elapsed > 0:
                    estimated_total = elapsed / (completed / total_tasks)
                    remaining_time = estimated_total - elapsed
                else:
                    remaining_time = 0

                print(f"📈 进度: {progress:.1f}% ({completed}/{total_tasks}), "
                      f"总解数: {total_solutions}, "
                      f"用时: {elapsed:.1f}s, "
                      f"预计剩余: {remaining_time:.1f}s")

                last_progress_time = current_time

    end_time = time.time()
    total_solutions = writer.get_count()
    writer.write_footer()

    print(f"✅ 求解完成!")
    elapsed_time = end_time - start_time
    print(f"⏱️  总耗时: {elapsed_time:.2f} 秒")
    print(f"🎯 总解数: {total_solutions}")
    print(f"📁 解已保存到: {filename}")

    if os.path.exists(filename):
        print(f"📊 文件大小: {os.path.getsize(filename) / 1024:.1f} KB")

    if elapsed_time > 0:
        print(f"🎯 求解速度: {total_solutions / elapsed_time:.1f} 解/秒")
    else:
        print(f"🎯 求解速度: 极快 (耗时 < 0.01秒)")

    return total_solutions


def validate_constraints(solution, x, n):
    """
    验证解是否满足所有约束条件
    """
    total_sum = sum(solution)
    weighted_sum = sum(i * solution[i] for i in range(1, x))
    non_increasing = all(solution[i] >= solution[i + 1] for i in range(x - 1))
    all_positive = all(a >= 1 for a in solution)

    # 新约束（只检查前三个变量）
    new_constraints_ok = True
    for i in range(min(3, x)):
        max_val = get_max_value_constraint(i, n)
        if solution[i] > max_val:
            new_constraints_ok = False
            break

    return (total_sum == n and weighted_sum == n and
            non_increasing and all_positive and new_constraints_ok)


if __name__ == "__main__":
    print("🎯 带新约束条件的组合优化求解器 (防内存爆炸版)")
    print("约束: a_i ≤ max((0.5)^(i+1) * n, 1) 仅对 i=0,1,2 生效")
    print("=" * 55)

    x = int(input("请输入变量个数 x: "))
    n = int(input("请输入 n: "))

    # 显示约束信息
    print(f"\n📏 约束条件预览:")
    for i in range(x):
        if i <= 2:
            max_val = get_max_value_constraint(i, n)
            formula_power = i + 1
            actual_calc = (0.5 ** formula_power) * n
            print(f"   a{i} ≤ max((0.5)^{formula_power} * {n}, 1) = max({actual_calc:.2f}, 1) = {max_val}")
        else:
            print(f"   a{i} 无额外约束 (仅受递减和正整数约束)")

    print("\n选择求解方式:")
    print("1. 单线程 (直接写文件)")
    print("2. 基础多线程 (直接写文件)")
    print("3. 高级多线程 (直接写文件)")

    choice = input("请选择 (1-3): ").strip()

    print(f"\n🎯 开始求解 x={x}, n={n}...")
    print("=" * 40)

    start_time = time.time()

    if choice == "1":
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"solutions_constrained_single_x{x}_n{n}_{timestamp}.txt"
        writer = SolutionWriter(filename, x, n, "带约束单线程")
        total_solutions = find_all_solutions_with_constraints_single_thread(x, n, writer)
        writer.write_footer()

        print(f"\n✅ 求解完成!")
        print(f"🎯 总解数: {total_solutions}")
        print(f"📁 解已保存到: {filename}")

    elif choice == "2":
        total_solutions = find_all_solutions_with_constraints_multithread(x, n)

    elif choice == "3":
        total_solutions = find_all_solutions_with_constraints_advanced_multithread(x, n)

    else:
        print("无效选择，使用高级多线程模式")
        total_solutions = find_all_solutions_with_constraints_advanced_multithread(x, n)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\n⏱️  总耗时: {elapsed_time:.2f} 秒")

    if total_solutions > 0 and elapsed_time > 0:
        print(f"🎯 平均求解速度: {total_solutions / elapsed_time:.1f} 解/秒")