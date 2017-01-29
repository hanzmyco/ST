# -*- coding: utf-8 -*-
'''
用2^n次方来循环，每次看看数字i的第Index位是不是1，如果是1，那么就
把num[index]加入到当前这个set里
'''

def subsets(nums):
    l=pow(2,len(nums))
    output=[[]]
    for i in xrange(1,l):
        li=[]
        for index in xrange(0,len(nums)):
            if i >> index & 1 ==1:
               li.append(nums[index])
        output.append(li)
    print output

subsets([1,2,3])