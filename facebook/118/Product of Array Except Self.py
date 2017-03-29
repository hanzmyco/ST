# -*- coding: utf-8 -*-
'''
res 一开始存每个数左边的乘积
然后从右边起用right存除了右边的，然后乘起来
'''
def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = [1]
    for i in xrange(1, len(nums)):
        res.append(res[i - 1] * nums[i - 1])
    right = 1
    for i in xrange(len(nums) - 1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res