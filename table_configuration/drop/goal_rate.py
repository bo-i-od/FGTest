import random
import numpy as np







def simulate_once(probs, scores, n_rounds, threshold):
    """
    模拟一次玩家游玩 n_rounds 局，返回平均得分
    probs: 各分数口的概率 [p1, p2, ...]
    scores: 对应的得分 [s1, s2, ...]
    n_rounds: 模拟多少局（币数）
    threshold: 保底阈值 (亏损<-threshold时触发一次200)
    """
    expected_single = sum(p * s for p, s in zip(probs, scores))
    total_score = 0
    cumulative_loss = 0  # 实际得分 - 期望得分

    for _ in range(n_rounds):
        # 检查是否触发保底
        if cumulative_loss <= -threshold:
            score = 150  # 强制大奖
        else:
            score = random.choices(scores, weights=probs, k=1)[0]

        total_score += score
        cumulative_loss += (score - expected_single)

    return total_score / n_rounds  # 平均得分（每币）


def estimate_expectation(probs, scores, threshold, n_rounds=10000, n_trials=1000):
    """
    多次模拟以估算平均期望
    """
    results = [simulate_once(probs, scores, n_rounds, threshold) for _ in range(n_trials)]
    return np.mean(results), np.std(results)

def simulate_expectation_with_safety_net(
    scores,           # 得分列表，如 [1, 10, 20, 200]
    probs,            # 对应概率，如 [0.332, 0.4, 0.2, 0.068]
    threshold,        # 保底触发阈值（负值，如 -200）
    total_rounds=100_000,  # 总模拟局数（越大越准）
    verbose=False     # 是否打印过程
):
    """
    模拟带保底机制下的长期平均期望得分
    """
    if len(scores) != len(probs):
        raise ValueError("scores 和 probs 长度必须相等")
    if abs(sum(probs) - 1.0) > 1e-6:
        raise ValueError("probs 总和必须为 1")

    # 原始无保底期望
    original_expectation = sum(s * p for s, p in zip(scores, probs))
    if verbose:
        print(f"原始期望得分: {original_expectation:.3f}")

    cumulative_loss = 0.0   # 累计亏损 = 实际总分 - 期望总分
    total_score = 0.0       # 实际总得分
    next_is_bonus = False   # 下一局是否强制触发保底

    for i in range(total_rounds):
        if next_is_bonus:
            score = 200
            next_is_bonus = False
            # 触发后清零亏损（你也可以选择不清零，改为 += bonus_score - original_expectation）
            cumulative_loss = 0.0
        else:
            # 正常随机抽取
            r = random.random()
            cum_prob = 0.0
            score = scores[0]
            for j, p in enumerate(probs):
                cum_prob += p
                if r < cum_prob:
                    score = scores[j]
                    break


        total_score += score
        cumulative_loss += score - original_expectation

        # 检查是否触发保底（下一次）
        if cumulative_loss <= -threshold:
            next_is_bonus = True
            if verbose and i < 10000:  # 只打印前100次内的触发，避免刷屏
                print(f"第{i+1}局后触发保底，累计亏损={cumulative_loss:.1f}")

    final_expectation = total_score / total_rounds
    uplift = final_expectation - original_expectation

    if verbose:
        print(f"\n模拟完成：{total_rounds} 局")
        print(f"带保底机制后期望得分: {final_expectation:.3f}")
        print(f"相比原始期望提升: {uplift:+.3f}")

    return final_expectation


def main():
    # # 先定下中间的两个概率求大奖
    goal_rate = {13: 0.3, 24: 0.3}
    expect_convert_rate = 32
    expect_collision_times = 1
    remain = expect_convert_rate - expect_collision_times * 8
    remain -= goal_rate[13] * 13 + goal_rate[24] * 24
    # (1 - goal_rate[13] - goal_rate[24] - x) * 100 + 2x = remain
    x = (150 * (1 - goal_rate[13] - goal_rate[24]) - remain) / 148
    y = 1 - goal_rate[13] - goal_rate[24] - x
    print(x, y)
    # convert_rate_bad = goal_rate[10] * 10 + goal_rate[20] * 20 + 1 - goal_rate[10] - goal_rate[20]
    # print(convert_rate_bad)

    # ===== 使用示例 =====
    probs = [0.315, 0.3, 0.304, 0.081]  # 概率
    scores = [2, 13, 24, 150]  # 对应分数
    threshold = 75  # 保底阈值：累计亏分超过200触发

    # mean, std = estimate_expectation(probs, scores, threshold)
    # print(f"带保底规则的一次期望得分 ≈ {mean:.3f} (±{std:.3f})")

    exp = simulate_expectation_with_safety_net(
        scores, probs, threshold,
        total_rounds=500_000,  # 提高精度
        verbose=True
    )
    print(exp)



# 示例使用
if __name__ == "__main__":
    main()