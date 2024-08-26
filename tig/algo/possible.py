from random import random

from tig.algo.dp_1d import knapsack_dp_comp
from tig.algo.generate_instance import Difficulty, generate_instance

if __name__ == '__main__':
    num_items = 100
    better_than_baseline = 10
    difficulty = Difficulty(num_items, better_than_baseline)

    for p in range(10000):

        seeds = [random()] * 8
        c = generate_instance(seeds, difficulty)
        weights = c.weights
        values = c.values
        capacity = c.capacity
        n = c.difficulty.num_items

        # 一维 dp
        res4 = knapsack_dp_comp(weights, values, capacity)

        print(p)
        if res4 >= c.passing_value:
            print("有解")
