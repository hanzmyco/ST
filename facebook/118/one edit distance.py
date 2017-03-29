# -*- coding: utf-8 -*-
'''
开始遍历每个点，如果s[i]!=t[i], 那么如果长度一样，就比较后面看看是不是一样
如果长度不一样，那么就比较长的那个从后一位开始和短的比
'''



def isOneEditDistance(s,t):
    for i in xrange(0,min(len(s),len(t))):
        if s[i]!=t[i]:
            if len(s) == len(t):
                return s[i+1:] == t[i+1:]
            elif len(s)<len(t):
                return s[i:] == t[i+1:]
            else:
                return s[i+1:] ==t[i:]

    return abs(len(s)-len(t))==1