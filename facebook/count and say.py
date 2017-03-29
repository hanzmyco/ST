# -*- coding: utf-8 -*-
'''
对老词进行递归，每次看看连续相当的有几个，每次在新词上加上2个，然后赋新词给老词，
赋予新长度给老长度
'''
def get_result(n):
    old_str='1'
    while n-1>0:
        sb=''
        l=len(old_str)
        i=0
        while i<l:
            count=1
            while i+1 < l and old_str[i]==old_str[i+1]:
                count+=1
                i+=1
            sb+=str(count)+old_str[i]
            i+=1
        old_str=sb
        n-=1
    return old_str
print get_result(4)

