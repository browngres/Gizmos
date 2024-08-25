def knapsack_dfs(w: list[int], v: list[int], n: int, c: int) -> int:
    """0-1 背包：暴力搜索
    时间复杂度 0（2^n），超过 25 要费很长时间。疯狂重复递归
    """
    "https://www.hello-algo.com/chapter_dynamic_programming/knapsack_problem/#1"
    # 若已选完所有物品或背包无剩余容量，则返回价值 0
    if n == 0 or c == 0:
        return 0
    # 若超过背包容量，则只能选择不放入背包
    if w[n - 1] > c:
        return knapsack_dfs(w, v, n - 1, c)
    # 计算不放入和放入物品 i 的最大价值
    no = knapsack_dfs(w, v, n - 1, c)
    yes = knapsack_dfs(w, v, n - 1, c - w[n - 1]) + v[n - 1]
    # 返回两种方案中价值更大的那一个
    return max(no, yes)
