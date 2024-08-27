from random import random

# from tig.algo.brute_force import brute_force
# from tig.algo.dfs import knapsack_dfs
from tig.algo.dfs_mem import knapsack_dfs_mem
from tig.algo.dp_1d_selected import knapsack_dp_select
from tig.algo.dp_2d import knapsack_dp
from tig.algo.dp_1d import knapsack_dp_comp
from tig.algo.annealing import annealing_algorithm

from tig.algo.generate_instance import Difficulty, generate_instance

if __name__ == '__main__':
    num_items = 60
    better_than_baseline = 25
    difficulty = Difficulty(num_items, better_than_baseline)
    # seeds = [0] * 8
    seeds = [random()] * 8
    c = generate_instance(seeds, difficulty)

    '''
    案例：seed = [0]*8  和 n=10 
    weight： [49, 3, 25, 33, 25, 26, 3, 33, 3, 26]
    value： [31, 25, 31, 3, 38, 25, 38, 3, 33, 25]
    背包容量： 113
    总重： 226
    基准难度： 0
    贪心基准线： 215
    价值密度排序 [6, 8, 1, 4, 2, 5, 9, 0, 3, 7]
    标准答案 [6, 8, 1, 4, 2, 5, 9]
    '''
    weights = c.weights
    values = c.values
    capacity = c.capacity
    n = c.difficulty.num_items

    # key = [6, 8, 1, 4, 2, 5, 9]
    # print("======答案=========")
    # c.verify_solution(key)
    print("===============")
    # 暴力求解
    # best_v, best_combination = brute_force(c)
    # selected = [index for index, value in enumerate(best_combination) if value == 1]
    # print(selected)

    # 暴力求解 dfs
    # res1 = knapsack_dfs(c.weights,c.values,c.difficulty.num_items,c.capacity)
    # print("暴力求解 dfs：", res1)

    '''
    # 暴力求解 dfs_mem
    mem = [[-1] * (capacity + 1) for _ in range(n + 1)]
    res2 = knapsack_dfs_mem(weights, values, mem, n, capacity)
    print("暴力求解 dfs：", res2)

    # 二维 dp
    res3 = knapsack_dp(weights, values, capacity)
    print("二维 dp：", res3)
    '''
    # 一维 dp
    res4 = knapsack_dp_comp(weights, values, capacity)
    print("一维 dp：", res4)

    # 一维 dp 带选择
    res5, res5_selected = knapsack_dp_select(weights, values, capacity)
    print("一维 dp 带选择的结果：", res5)
    print("一维 dp 带选择的挑选：", res5_selected)
    print("一维 dp 带选择的挑选个数：", len(res5_selected))

    # 退火
    # best_v, best = annealing_algorithm(c, init_temp=100, steps=1000)
    # selected = [index for index, value in enumerate(best) if value == 1]
    # print(selected)
    # c.verify_solution(selected)

