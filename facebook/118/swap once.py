# -*- coding: utf-8 -*-
'''
从右往左存当前见过的最大值，
第二遍循环从头开始只要最大值和本身不一样，那么久交换
'''


from collections import deque
def swap_once(nums):
    maxx=len(nums)-1
    max_arr=deque()
    max_arr.append(len(nums)-1)

    for i in xrange(len(nums)-2,-1,-1):
        if nums[i] >= nums[maxx]:
            maxx=i
        max_arr.appendleft(maxx)
    for i in xrange(0,len(max_arr)):
        if max_arr[i] != i:
            swap(nums,i,max_arr[i])
            break


    print nums




def swap(nums,i,j):
    temp=nums[i]
    nums[i]=nums[j]
    nums[j]=temp

nums=[4,2,1,3,4]
#nums=[4,4,4,4,3,4]
swap_once(nums)