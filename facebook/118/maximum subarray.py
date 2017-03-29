import sys
def maxSubArray(nums):
    res=-sys.maxint-1
    curSum=0
    for ite in nums:
        curSum+=ite
        curSum=max(curSum,ite)
        res=max(res,curSum)
    return res