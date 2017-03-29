# -*- coding: utf-8 -*-
'''
初始化名人为0，从1开始，看看名人认不认识他，认识的话，名人变为i，再从头来看，从头检查，如果res认识这个人或者不被人认识，那么就返回-1
'''



def findCelebrity(n):
    res=0
    for i in xrange(0,n):
        if knows(res,i):
            res=i
    for i in xrange(0,n):
        if i!=res and knows(res,i) or knows(i,res)==False :
            return -1

    return res


