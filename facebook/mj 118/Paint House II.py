def minCostII(costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    n = len(costs)
    if n == 0:
        return 0
    k = len(costs[0])
    dp = [[]]
    for i in xrange(0, k):
        dp[0].append(costs[0][i])
    for i in xrange(1, n):
        dp.append([])
        for j in xrange(0, k):
            res = 100000
            for c in xrange(0, k):
                if c != j:
                    res = min(res, dp[i - 1][c])
            dp[i].append(res + costs[i][j])
    return min(dp[n - 1])