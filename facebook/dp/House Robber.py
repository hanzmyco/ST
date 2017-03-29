# -*- coding: utf-8 -*-
'''
dp, dp[i]=max(dp[i-2]+nums[i] , dp[i-1])
dp[i-2]相当于偷到i-2为止，i-2可偷可不偷，算dp[i]的时候肯定要偷 i
dp[i-1]的时候相当于偷到i-1，i-1可偷可不偷，所以这两者的max覆盖了所有可能情况

'''

def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    leng = len(nums)
    if leng == 0:
        return 0
    elif leng == 1:
        return nums[0]

    dp = [nums[0],max(nums[0],nums[1])]

    for i in xrange(2, leng):
        current=max(dp[0]+nums[i],dp[1])
        dp[0]=dp[1]
        dp[1]=current
    return dp[1]