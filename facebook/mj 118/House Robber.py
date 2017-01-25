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