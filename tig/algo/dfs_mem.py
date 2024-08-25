def knapsack_dfs_mem(
        w: list[int], v: list[int], mem: list[list[int]], n: int, c: int) -> int:
    """0-1 背包：记忆化搜索
    我们借助记忆列表 mem 来记录子问题的解，其中 mem[i][c] 对应 dp[i][c]
    """
    # 若已选完所有物品或背包无剩余容量，则返回价值 0
    if n == 0 or c == 0:
        return 0
    # 若已有记录，则直接返回
    if mem[n][c] != -1:
        return mem[n][c]
    # 若超过背包容量，则只能选择不放入背包
    if w[n - 1] > c:
        return knapsack_dfs_mem(w, v, mem, n - 1, c)
    # 计算不放入和放入物品 i 的最大价值
    no = knapsack_dfs_mem(w, v, mem, n - 1, c)
    yes = knapsack_dfs_mem(w, v, mem, n - 1, c - w[n - 1]) + v[n - 1]
    # 记录并返回两种方案中价值更大的那一个
    mem[n][c] = max(no, yes)
    return mem[n][c]
