# -*- coding: utf-8 -*-
'''
reduce 会循环的把结果作为第一个argument做下去
'''


def titleToNumber(self, s):
    """
    :type s: str
    :rtype: int
    """
    return reduce(lambda x, y: x * 26 + y, [ord(c) - 64 for c in list(s)])
