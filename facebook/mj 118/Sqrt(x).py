# -*- coding: utf-8 -*-
'''
二分，看看中间那个的平方如果小于= x，start=mid，否则反之
也是相差两个为止，
'''


def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    start = 1
    end = x
    while start < end - 1:
        mid = (start + end) / 2
        if mid * mid <= x:
            start = mid
        else:
            end = mid
    if end * end <= x:
        return int(end)
    return int(start)