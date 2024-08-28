def knapsack_dp_select(w: list[int], v: list[int], cap: int) -> tuple[int, list[int]]:
    """0-1 背包：空间优化后的动态规划，返回最大价值及选中的物品索引"""
    n = len(w)
    dp = [0] * (cap + 1)
    # 用于跟踪每个容量下的选择
    selected_items = [[] for _ in range(cap + 1)]

    for i in range(1, n + 1):
        for c in range(cap, w[i-1] - 1, -1):
            if w[i - 1] <= c:
                # 如果选择当前物品 i
                if dp[c] < dp[c - w[i - 1]] + v[i - 1]:
                    dp[c] = dp[c - w[i - 1]] + v[i - 1]
                    # 更新选中物品列表
                    selected_items[c] = selected_items[c - w[i - 1]] + [i - 1]

    return dp[cap], selected_items[cap]