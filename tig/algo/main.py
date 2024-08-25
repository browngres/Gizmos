from select import select

# from tig.algo.annealing import annealing_algorithm
from tig.algo.dfs import knapsack_dfs
# from tig.algo.brute_force import brute_force
from tig.algo.generate_instance import Difficulty, generate_instance

if __name__ == '__main__':
    num_items = 15
    better_than_baseline = 0
    difficulty = Difficulty(num_items, better_than_baseline)
    seeds = [0] * 8
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

    # key = [6, 8, 1, 4, 2, 5, 9]
    # 暴力求解
    # best_v, best_combination = brute_force(c)
    # selected = [index for index, value in enumerate(best_combination) if value == 1]
    # print(selected)

    # 暴力求解 dfs
    res = knapsack_dfs(c.weights,c.values,c.difficulty.num_items,c.capacity)
    print("暴力求解：", res)
    # 退火
    # best_v, best = annealing_algorithm(c, init_temp=100, steps=1000)
    # selected = [index for index, value in enumerate(best) if value == 1]
    # print("======答案=========")
    # c.verify_solution(key)
    # print("===============")
    # print(selected)
    # c.verify_solution(selected)
