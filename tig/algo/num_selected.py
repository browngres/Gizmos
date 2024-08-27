from threading import Thread

from tig.algo.dfs_mem import knapsack_dfs_mem
from tig.algo.generate_instance import Difficulty, generate_instance, RngArray

if __name__ == '__main__':
    TEST_COUNT = 100
    num_items = 100
    better_than_baseline = 0
    difficulty = Difficulty(num_items, better_than_baseline)

    selected_count = [0] * TEST_COUNT


    def get_selected_num(i):
        """
        求解一次贪心选择的数量
        """
        seeds = [i] * 8
        rngs = RngArray(seeds)
        rng = rngs.get_mut()
        n = difficulty.num_items
        weights = [rngs.get_mut().randint(1, 49) for _ in range(n)]
        values = [rngs.get_mut().randint(1, 49) for _ in range(n)]
        capacity = sum(weights) // 2

        sorted_v_to_w_ratio = list(range(n))
        sorted_v_to_w_ratio.sort(key=lambda x: values[x] / weights[x], reverse=True)

        total_weight = 0
        greedy_value = 0
        greedy_selected = []

        for item in sorted_v_to_w_ratio:
            if total_weight + weights[item] > capacity:
                continue
            greedy_value += values[item]
            total_weight += weights[item]
            greedy_selected.append(item)
        selected_count[i] = len(greedy_selected)


    for i in range(TEST_COUNT):
        t = Thread(target=get_selected_num, args=(i,), name=f'Thread_{i}')
        t.start()

    print(selected_count)
    avg = sum(selected_count) / len(selected_count)
    print("平均百分位：", 100 * avg / num_items)
    print("最大值百分位：", 100 * max(selected_count) / num_items)
    print("最小值百分位：", 100 * min(selected_count)/num_items)

    # 问题规模 60-100 之内， 贪婪选取百分位平均值恰恰在 62-64% 。

    # 95% 置信区间
    import numpy as np
    import scipy.stats as st
    print(st.norm.interval(confidence=0.95, loc=np.mean(selected_count), scale=st.sem(selected_count)))
