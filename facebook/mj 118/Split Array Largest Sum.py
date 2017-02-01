# -*- coding: utf-8 -*-
'''
二分式的查找看看能不能被分成，
'''

def split(nums,m,mid):
    res=0
    count=1
    for ite in nums:
        if res+ite <=mid:
            res+=ite
        else:
            count+=1
            res=ite
            if count >m:
                return False
    return True

def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    l=max(nums)
    r=sum(nums)
    while l < r-1:
        mid = l + (r - l) / 2
        if split(nums, m, mid):
            r = mid
        else:
            l = mid + 1
    if split(nums,m,l):
        return l
    return r


def can_split(nums, m, ssum):
    cnt = 1
    curSum = 0
    for i in xrange(0, len(nums)):
        curSum += nums[i]
        if curSum > ssum:
            curSum = nums[i]
            cnt += 1
            if cnt > m:  # ssum定的太小，所以l=mid_1
                return False
    return True

nums=[7,2,5,10,8]
m=2
print splitArray(nums,m)