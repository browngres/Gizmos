import math

from tig.algo.dp_1d import knapsack_dp_comp
from tig.algo.dp_1d_selected import knapsack_dp_select

if __name__ == '__main__':
    # rust   seed 666   n 60
    weights = [10, 10, 43, 10, 15, 11, 18, 10, 41, 10, 17, 10, 12, 10, 27, 43, 43, 15, 43, 18, 15, 15, 18, 18, 41, 43, 41,
             15, 41, 18, 17, 43, 17, 15, 17, 18, 12, 43, 12, 15, 12, 18, 27, 17, 17, 18, 22, 41, 41, 17, 41, 12, 17, 17,
             12, 12, 27, 18, 48, 27]
    values = [22, 17, 44, 18, 40, 17, 39, 27, 48, 18, 20, 22, 48, 22, 44, 40, 48, 44, 39, 17, 49, 43, 27, 44, 20, 49, 15,
            27, 40, 40, 39, 18, 23, 39, 22, 23, 20, 25, 17, 25, 18, 31, 22, 31, 48, 20, 30, 48, 49, 18, 49, 41, 44, 3,
            17, 23, 23, 25, 44, 3]

    n = len(weights)
    capacity = sum(weights) // 2

    sorted_v_to_w_ratio = list(range(n))
    sorted_v_to_w_ratio.sort(key=lambda x: values[x] / weights[x], reverse=True)
    print("价值密度排序：", sorted_v_to_w_ratio)

    greedy_value = 0
    limit1 = 0.0
    limit1_flag = True
    limit2 = 0.0
    limit2_flag = 0
    remain = capacity

    for i in range(n):
        item = sorted_v_to_w_ratio[i]
        if weights[item] > remain:
            # 拿不下
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

    print("limit1：", limit1)
    print("limit2：", limit2)
    print("预测最优解：", math.ceil(0.62*limit1 + 0.38*limit2))  # 乐观向上
    print("贪心基准线：", greedy_value)


    # 一维 dp
    res4 = knapsack_dp_comp(weights, values, capacity)
    print("一维 dp：", res4)

    # 一维 dp 带选择
    res5, res5_selected = knapsack_dp_select(weights, values, capacity)
    print("一维 dp 带选择的结果：", res5)
    print("一维 dp 带选择的挑选：", res5_selected)
    print("一维 dp 带选择的挑选个数：", len(res5_selected))