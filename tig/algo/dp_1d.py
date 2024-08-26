def knapsack_dp_comp(w: list[int], v: list[int], cap: int) -> int:
    """0-1 背包：空间优化后的动态规划"""
    n = len(w)
    # 初始化 dp 表
    dp = [0] * (cap + 1)
    # 状态转移
    for i in range(1, n + 1):
        # 倒序遍历
        for c in range(cap, w[i-1]-1, -1):
            if w[i - 1] > c:
                # 若超过背包容量，则不选物品 i
                dp[c] = dp[c]
            else:
                # 不选和选物品 i 这两种方案的较大值
                dp[c] = max(dp[c], dp[c - w[i - 1]] + v[i - 1])
    return dp[cap]