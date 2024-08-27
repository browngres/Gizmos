import math
from random import random

from tig.algo.dp_1d_selected import knapsack_dp_select
from tig.algo.generate_instance import RngArray

if __name__ == '__main__':
    num_items = 100
    better_than_baseline = 10
    # seeds = [135] * 8  # 60 & 135
    seeds = [random()] * 8
    # 生成案例
    rngs = RngArray(seeds)
    rng = rngs.get_mut()
    n = num_items
    weights = [rngs.get_mut().randint(1, 49) for _ in range(n)]
    values = [rngs.get_mut().randint(1, 49) for _ in range(n)]
    capacity = sum(weights) // 2
    print("weight：", weights)
    print("value：", values)
    print("背包容量：", capacity)

    #  贪心算法给出一个值
    sorted_v_to_w_ratio = list(range(n))
    sorted_v_to_w_ratio.sort(key=lambda x: values[x] / weights[x], reverse=True)
    print("价值密度排序：", sorted_v_to_w_ratio)
    greedy_value = 0
    greedy_selected = []
    limit1 = 0.0
    limit1_flag = True
    limit2_flag = 0
    limit2 = 0.0

    remain = capacity
    # 123
    for i in range(n):
        item = sorted_v_to_w_ratio[i]
        if weights[item] > remain:
            # 拿不下
            print(f"出现拿不下{item}，当前贪心拿了 {len(greedy_selected)} 个, 总重：{capacity-remain}")
            print(f"这个价值密度为： ", values[item] / weights[item])
            if limit1_flag and (i > 0):
                # 第一次出现拿不下，算出最优解的理论上限
                # 根据前一次猜测最大值
                last = sorted_v_to_w_ratio[i - 1]   # 乐观就选前一个，偏大
                # last = sorted_v_to_w_ratio[i]          # 不乐观选当前的
                print("计算 limit1 的item：", last)
                limit1 = greedy_value + remain * values[last] / weights[last]
                limit1_flag = False
                continue
            limit2_flag += 1
            if limit2_flag == 1:
                # 拿的下之后的第一次拿不下。算出最优解理论下限。
                # last = sorted_v_to_w_ratio[i - 1]
                last = sorted_v_to_w_ratio[i]
                print("计算 limit2 的item：", last)
                limit2 = greedy_value + remain * values[last] / weights[last]
            continue
        limit2_flag = 0
        greedy_value += values[item]
        remain -= weights[item]
        greedy_selected.append(item)

    print("limit1：", limit1)
    print("limit2：", limit2)
    print("预测最优解：", math.ceil(0.62*limit1 + 0.38*limit2))  # 乐观向上
    # print("预测最优解：", round(0.5 * (limit1 + limit2)))
    # print("greedy selected：", greedy_selected)
    greedy_selected.sort()
    # print("greedy selected sorted：", greedy_selected)
    # print("greedy selected 数量：", len(greedy_selected))
    print("贪心基准线：", greedy_value)

    # 一维 dp 带选择
    res5, res5_selected = knapsack_dp_select(weights, values, capacity)
    print("一维 dp 带选择的结果：", res5)
    # print("一维 dp 带选择的挑选：", res5_selected)
    # print("一维 dp 带选择的挑选个数：", len(res5_selected))
