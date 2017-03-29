# -*- coding: utf-8 -*-
'''
dp[0]=1 相当于什么都不拿，然后dp[i]+=dp[i-a], for a in nums
'''
def combinationSum4(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    dp = [1]
    if len(nums) == 0:
        return 0
    for i in xrange(1, target + 1):
        dp.append(0)
        for a in nums:
            if i >= a:
                dp[i] += dp[i - a]
    return dp[target]