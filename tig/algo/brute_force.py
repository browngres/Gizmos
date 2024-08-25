from itertools import combinations

from tig.algo.generate_instance import Challenge


def brute_force(challenge: Challenge):
    """暴力求解，下面的算法有问题，结果不对
    :param challenge: Challenge
    :return: tuple like: (best value, best combination list(contains 1 and 0))
    """
    number = challenge.difficulty.num_items
    # 数量超过 25 基本就算不出来了
    capacity = challenge.capacity
    weight_value = list(zip(challenge.weights, challenge.values))
    # 元组列表 [(weight, value), (weight, value), ...]
    best_v = None
    best_combination = []
    # generating combinations by all ways: C by 1 from n, C by 2 from n, ...
    for way in range(number):
        for comb in combinations(weight_value, way + 1):
            weight = sum([wv[0] for wv in comb])
            value = sum([wv[1] for wv in comb])
            if (best_v is None or best_v < value) and weight <= capacity:
                best_v = value
                best_combination = [0] * number
                for wv in comb:
                    best_combination[weight_value.index(wv)] = 1
    print("best value:", best_v)
    print("best combination:", best_combination)
    return best_v, best_combination