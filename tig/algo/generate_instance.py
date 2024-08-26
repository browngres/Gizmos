# 背包问题算法  用例
import random


class Difficulty:
    # 难度（两个参数）
    def __init__(self, num_items: int, better_than_baseline: int):
        self.num_items = num_items
        self.better_than_baseline = better_than_baseline


class RngArray:
    # 随机数组
    def __init__(self, seeds: list):
        # 使用给定的种子初始化8个随机数生成器
        self.rngs = [random.Random(seed) for seed in seeds]
        self.index = 0

    def get_mut(self):
        # 使用当前索引的随机数生成器生成一个0到7之间的随机索引
        self.index = self.rngs[self.index].randint(0, 7)
        # 返回当前索引的随机数生成器
        return self.rngs[self.index]


class Challenge:
    def __init__(self, seeds, difficulty, weights, values, capacity, passing_value):
        self.seeds = seeds
        self.difficulty = difficulty
        self.weights = weights
        self.values = values
        self.capacity = capacity
        self.passing_value = passing_value

    def verify_solution(self, selected):
        if len(set(selected)) != len(selected):
            raise Exception("选择列表有重复")
        for i in selected:
            if i >= self.difficulty.num_items:
                raise IndexError("选择列表越界")
        # 计算选定物品的总重量
        total_w = sum(self.weights[i] for i in selected)
        print(f"select 总重：{total_w}")
        # 检查总重量是否超过最大容量
        if total_w > self.capacity:
            raise ValueError(f"超重： {total_w} > {self.capacity}")
        # 计算选定物品的总价值
        total_v = sum(self.values[i] for i in selected)
        print(f"select 总价值：{total_v}")
        if total_v < self.passing_value:
            raise ValueError(f"价值不足： {total_v} < {self.passing_value}")

        print("通过。")
        return True


def generate_instance(seeds, d: Difficulty):
    """
    :param seeds:  种子，长度为 8 的数组
    :param d:  难度
    :return:  返回重量、价值列表
    """
    # 初始化随机数生成器
    rngs = RngArray(seeds)
    # 获取一个随机数生成器，并从中生成随机数
    rng = rngs.get_mut()
    # 生成重量 [1, 49]
    n = d.num_items
    weights = [rngs.get_mut().randint(1, 49) for _ in range(n)]
    # 生成价值 [1, 49]
    values = [rngs.get_mut().randint(1, 49) for _ in range(n)]
    # 计算背包容量为总重量的一半
    capacity = sum(weights) // 2

    print("weight：", weights)
    print("value：", values)
    print("背包容量：", capacity)
    print("总重：", capacity * 2)

    #  贪心算法计算及格线

    # 生成物品索引的列表
    sorted_v_to_w_ratio = list(range(n))
    # 根据价值密度对物品索引进行降序
    sorted_v_to_w_ratio.sort(key=lambda x: values[x] / weights[x], reverse=True)

    # 遍历排序后的物品索引
    total_weight = 0
    greedy_value = 0
    greedy_selected = []
    for item in sorted_v_to_w_ratio:
        if total_weight + weights[item] > capacity:
            print(f"出现拿不下，当前贪心拿了 {len(greedy_selected)} 个, 总重：{total_weight}")
            print(f"这个价值密度为： ", values[item]/weights[item])
            continue
        greedy_value += values[item]
        total_weight += weights[item]
        greedy_selected.append(item)

    # print("greedy selected：", greedy_selected)
    greedy_selected.sort()
    print("greedy selected sorted：", greedy_selected)
    print("greedy selected 数量：", len(greedy_selected))
    print("基准难度：", d.better_than_baseline)
    print("贪心基准线：", greedy_value)
    passing_value = round(greedy_value * (1 + d.better_than_baseline / 1000))
    print("及格线：", passing_value)

    return Challenge(
        seeds,
        d,
        weights,
        values,
        capacity,
        passing_value
    )
