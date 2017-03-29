# -*- coding: utf-8 -*-
'''
start 和end如果只差一个就退出，而且是左闭右闭

'''


def findfirstbad(n):
    start=1
    end=n
    while start+1<end:
        mid=(start+end)/2
        if badversion(mid):
            end=mid
        else:
            start=mid
    if badversion(start):
        return start
    return end

def badversion(i):
    return True