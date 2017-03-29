# -*- coding: utf-8 -*-
'''
连续和，用一个map存连续和最后的位置，如果和k相等，更新res，
否则看看s-k在不在，在的话
那么更新res和 (i-map[s-k],res)
'''



def maxSubArrayLen(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    s = 0
    map = {}
    res = 0
    for i in xrange(0, len(nums)):
        s += nums[i]
        if s == k:
            res = i + 1
        elif s - k in map:
            res = max(res, i - map[s - k])
        if s not in map:
            map[s] = i
    return res