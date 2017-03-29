# -*- coding: utf-8 -*-
'''
先把最小和次小设为maxint，来到一个先看如果小于最小让它等于最小，
之后如果有比最小大但是比次小小的，让次小等于它，如果
来了一个比最小次小都大的，就返回True了
'''

import sys
def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    m1 = sys.maxint
    m2 = sys.maxint
    for ite in nums:
        if ite <= m1:
            m1 = ite
        elif ite <= m2:
            m2 = ite
        else:
            return True
    return False