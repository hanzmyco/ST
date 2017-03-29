# -*- coding: utf-8 -*-
'''
考虑额外的字符，其实没一个\n里， \t的数目就决定了第几层

'''

def lengthLongestPath(input):
    map={}
    res=0
    map[0]=0   # level 0
    for s in input.split('\n'):
        level=s.rfind('\t')+1
        length=len(s)-level
        if '.' in s:
            res=max(res,map[level]+length)
        else:
            map[level+1]=map.get(level)+length+1
    return res

s="dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
lengthLongestPath(s)