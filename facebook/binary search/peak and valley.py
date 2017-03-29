# -*- coding: utf-8 -*-
'''
二分法，找中间的，看看中间的是否大于中间两边的，然后开始二分一半区间，
注意如果left middle right是一条直线那么就可以退出了
'''

import random


def Binary_Access(nums,start,end,result):

    if start +1 < end:
        mid=start+(end-start)/2
        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1] or nums[mid]< nums[mid-1] and nums[mid] < nums[mid+1]:
            result.append(mid)
        if nums[mid]-nums[start] == abs(mid-start) and nums[mid] - nums[end] == abs(mid-end):
            return result
        if nums[mid] - nums[start] != abs(mid-start):
            Binary_Access(nums,start,mid,result)
        if nums[mid] - nums[end] != abs(mid-end):
            Binary_Access(nums,mid,end,result)


nums=[0]
for i in xrange(1,5):
    a=random.randint(0,1)
    if a:
        nums.append(nums[i-1]+1)
    else:
        nums.append(nums[i-1]-1)
print nums

result=[]
Binary_Access(nums,0,4,result)
print result


nums=[0]
for i in xrange(1,3):
    a=random.randint(0,1)
    if a:
        nums.append(nums[i-1]+1)
    else:
        nums.append(nums[i-1]-1)
print nums
result=[]
Binary_Access(nums,0,2,result)
print result
