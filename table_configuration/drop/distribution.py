import pulp

# 原始数据
# score_count = {0: 279, 1: 140, 2: 70, 3: 36, 4: 17, 5: 9, 6: 5, 7: 3, 8: 1}
# score_count = {0:140, 1:70, 2:35, 3:18, 4:7, 5:5, 6:3, 7:1, 8:1}
# score_count = {0: 38, 1: 20, 2: 10, 3: 5, 4: 2, 5: 1, 6: 1, 7: 2, 8: 1}
# score_count = {0: 81, 1: 69, 2: 35, 3: 31, 4: 25, 5: 20, 6: 10, 7: 5, 8: 3, 9: 1}
# [100, 70, 35, 29, 24, 12, 6, 3, 1]
# [121, 63, 28, 20, 16, 11, 8, 6, 4, 2, 1]
score_count = {0: 121, 1: 63, 2: 28, 3: 20, 4: 16, 5: 11, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1}
scores = sorted(score_count.keys())
counts = [score_count[i] for i in scores]
total_samples = sum(counts)  # 560

# 归一化原始分布比例
original_ratio = {s: score_count[s] / total_samples for s in scores}

# 目标平均分
target_avgs = [1.75, 1.65, 1.5, 1.4, 1.5, 1.65, 1.75]
# target_avgs = [1, 1]
num_groups = len(target_avgs)
group_size = 40

# 权重设置
WEIGHT_SCORE_ERROR = 10.0
WEIGHT_DISTRIBUTION = 1.0

# 创建问题
prob = pulp.LpProblem("MultiObjective_ScoreDistribution", pulp.LpMinimize)

# 决策变量
x = {}
for i in scores:
    for j in range(num_groups):
        x[i, j] = pulp.LpVariable(f"x_{i}_{j}", lowBound=0, cat='Integer')

# === 平均分误差部分 ===
dev_plus = {}
dev_minus = {}
for j in range(num_groups):
    # 修改变量名，避免特殊字符
    dev_plus[j] = pulp.LpVariable(f"dev_plus_{j}", lowBound=0)
    dev_minus[j] = pulp.LpVariable(f"dev_minus_{j}", lowBound=0)
    prob += (
        pulp.lpSum([i * x[i, j] for i in scores]) - target_avgs[j] * group_size
        == dev_plus[j] - dev_minus[j]
    )

# === 分布相似度部分 ===
dist_dev_pos = {}
dist_dev_neg = {}
for j in range(num_groups):
    for s in scores:
        dist_dev_pos[s, j] = pulp.LpVariable(f"dist_pos_{s}_{j}", lowBound=0)
        dist_dev_neg[s, j] = pulp.LpVariable(f"dist_neg_{s}_{j}", lowBound=0)
        expected_count = round(original_ratio[s] * group_size)
        prob += (x[s, j] - expected_count) == dist_dev_pos[s, j] - dist_dev_neg[s, j]

# ==== 目标函数 ====
score_error_term = pulp.lpSum(dev_plus[j] + dev_minus[j] for j in range(num_groups))
distribution_term = pulp.lpSum(dist_dev_pos[s, j] + dist_dev_neg[s, j] for s in scores for j in range(num_groups))
prob += WEIGHT_SCORE_ERROR * score_error_term + WEIGHT_DISTRIBUTION * distribution_term

# ==== 约束 ====
for j in range(num_groups):
    prob += pulp.lpSum(x[i, j] for i in scores) == group_size

for idx, i in enumerate(scores):
    prob += pulp.lpSum(x[i, j] for j in range(num_groups)) <= counts[idx]

# ==== 求解 ====
prob.solve()

# ==== 输出结果 ====
print("✅ 双目标优化结果")
if pulp.LpStatus[prob.status] != 'Optimal':
    print("⚠️  Warning: 未找到最优解，状态 =", pulp.LpStatus[prob.status])

total_score_err = 0
total_dist_err = 0

for j in range(num_groups):
    assigned = {i: int(round(x[i, j].varValue or 0)) for i in scores if (x[i, j].varValue or 0) > 0.5}
    actual_total_score = sum(k * v for k, v in assigned.items())
    actual_avg = actual_total_score / group_size if group_size > 0 else 0
    score_err = abs(actual_avg - target_avgs[j])
    total_score_err += score_err

    l1_dist = sum(abs(assigned.get(s, 0)/group_size - original_ratio[s]) for s in scores)
    total_dist_err += l1_dist

    print(f"Group {j}: {assigned}")
    print(f"         avg={actual_avg:.3f} (目标{target_avgs[j]}) Δscore={score_err:.3f}, L1_dist={l1_dist:.3f}")

print(f"\n📊 总平均分误差: {total_score_err:.3f}")
print(f"📊 总分布L1距离: {total_dist_err:.3f}")

# 验证总数
total_assigned = sum(sum(int(round(x[i, j].varValue or 0)) for j in range(num_groups)) for i in scores)
print(f"\n验证: 总分配数量 = {total_assigned} (应该 = {num_groups * group_size})")