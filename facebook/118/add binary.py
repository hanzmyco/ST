# -*- coding: utf-8 -*-
'''
从最右边开始+，res= str((anum+bnum+carry)%2) + res

'''

def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    index_a = len(a) - 1
    index_b = len(b) - 1
    if index_a == -1:
        return b
    if index_b == -1:
        return a
    carry = 0
    res = ''
    while index_a >= 0 or index_b >= 0:
        a_num = 0
        b_num = 0
        if index_a >= 0:
            a_num = int(a[index_a])
        if index_b >= 0:
            b_num = int(b[index_b])
        res = str((a_num + b_num + carry) % 2) + res
        carry = (a_num + b_num + carry) / 2
        if index_a>=0:
            index_a -= 1
        if index_b>=0:
            index_b -= 1
    if carry == 1:
        res = '1' + res
    return res