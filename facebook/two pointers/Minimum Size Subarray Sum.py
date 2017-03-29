# -*- coding: utf-8 -*-
'''
两个指针，右边不断往右，当 和 大于s时，开始减去左边，每成功
减去一次之后和当前最小的长度进行比较
'''

def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    res = 100000
    left = 0
    summ = 0
    for i in xrange(0, len(nums)):
        summ += nums[i]
        while left <= i and summ >= s:
            res = min(i - left + 1, res)
            summ -= nums[left]
            left += 1
    if res == 100000:
        return 0
    return res