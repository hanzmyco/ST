def maxSubArray(nums):
    res=-10000
    curSum=0
    for ite in nums:
        curSum+=ite
        curSum=max(curSum,ite)
        res=max(res,curSum)
    return res