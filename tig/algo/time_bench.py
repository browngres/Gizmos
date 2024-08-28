import time
from random import random

from tig.algo.dfs_mem import knapsack_dfs_mem
from tig.algo.dp_1d import knapsack_dp_comp
from tig.algo.dp_1d_selected_2d import knapsack_dp_select
from tig.algo.generate_instance import Difficulty, generate_instance

# 测试性能

if __name__ == '__main__':
    num_items = 60
    difficulty = Difficulty(num_items, 0)

    seeds = [random()] * 8
    c = generate_instance(seeds, difficulty)
    weights = c.weights
    values = c.values
    capacity = c.capacity
    n = c.difficulty.num_items
    mem = [[-1] * (capacity + 1) for _ in range(n + 1)]

    N = 1  # 执行1次

    # 测试 dfs_mem
    total_time = 0.0
    for i in range(N):
        # seeds = [random()] * 8
        # c = generate_instance(seeds, difficulty)
        # weights = c.weights
        # values = c.values
        # capacity = c.capacity
        # n = c.difficulty.num_items
        # mem = [[-1] * (capacity + 1) for _ in range(n + 1)]
        start_time = time.perf_counter()
        knapsack_dfs_mem(weights, values, mem, n, capacity)
        end_time = time.perf_counter()
        total_time += end_time - start_time
    print(f'dfs_mem: {total_time:.4f} seconds')

    # 测试 dp_1d
    total_time = 0.0
    for i in range(N):
        # seeds = [random()] * 8
        # c = generate_instance(seeds, difficulty)
        # weights = c.weights
        # values = c.values
        # capacity = c.capacity
        start_time = time.perf_counter()
        knapsack_dp_comp(weights, values, capacity)
        end_time = time.perf_counter()
        total_time += end_time - start_time
    print(f'dp_1d: {total_time:.4f} seconds')

    # 非常神奇，如果只算 1 次 ，dfs 比 dp 慢。 重复算2次以上，dfs 就比 dp 快。
    # 如果把生成实例也加入循环，dp 就比dfs 快了。
    # 说明 python 确实在 dfs 中偷偷用缓存了
    # 真实情况就是 dp 肯定要比 dfs 快，规模越大越明显

    # 测试 1d_selected
    total_time = 0.0
    for i in range(N):
        start_time = time.perf_counter()
        knapsack_dp_select(weights, values, capacity)
        end_time = time.perf_counter()
        total_time += end_time - start_time
    print(f'dp_1d_selected: {total_time:.4f} seconds')

    # 对于目前的情况（0-1 背包，极大无解）时间显得不重要，必须拿到最优解
    """
    80 规模：
    dfs_mem: 0.0504 seconds
    dp_1d: 0.0219 seconds
    dp_1d_selected: 0.0291 seconds
    60规模：
    dfs_mem: 0.0152 seconds
    dp_1d: 0.0102 seconds
    dp_1d_selected: 0.0131 seconds
    """