# -*- coding: utf-8 -*-
'''
只需要保存上一轮（i-1）的最小值与此小值，对于新的一轮i，j从0到k，如果j和上一轮
min1坐标一样，就用上一轮min2的值，反之亦然。最后也是需要在过程中找到这一轮
的最小值与次小值
'''

import copy
def minCost(costs):
    n = len(costs)
    if n == 0:
        return 0
    k = len(costs[0])
    dp = copy.deepcopy(costs)
    min1,min2=-1,-1
    for i in xrange(0,n):
        last1,last2=min1,min2
        min1=-1
        min2=-1
        for j in xrange(0,k):
            if j!=last1:
                if last1>=0:
                    dp[i][j]+=dp[i-1][last1]
            else:
                if last2>=0:
                    dp[i][j]+=dp[i-1][last2]
            if min1 < 0 or dp[i][j] < dp[i][min1]:
                min2=min1
                min1=j
            elif min2<0 or dp[i][j] < dp[i][min2]:
                min2=j
    return min(dp[n-1])






nums=[1,2,3,3,1]
minCost(nums)

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

