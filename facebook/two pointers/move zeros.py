# -*- coding: utf-8 -*-
'''
记录下有多少个0，遇到不是0的就往前挪前面有多少个零个，这是最少次数的移动方法
'''

def moveZeros(nums):
    y=0
    for x in xrange(0,len(nums)):
        if nums[x]:
            if nums[x]!=nums[y]:
                nums[x], nums[y] = nums[y],nums[x]
            y+=1
    print nums

def two_pointers(nums):
    left=0
    right=0
    numofwrite=0
    while right< len(nums):
        if nums[right]!=0 :
            if nums[left]==0:
                temp=nums[right]
                nums[right]=nums[left]
                nums[left]=temp
                numofwrite+=2
            left+=1
        right+=1
    print nums
    print numofwrite
def least_move(nums):
    zero_num=0
    numofwrite=0
    for i in xrange(0,len(nums)):
        if nums[i]==0:
            zero_num+=1
        else:
            nums[i-zero_num]=nums[i]
            numofwrite+=1

    for i in xrange(len(nums)-zero_num,len(nums)):
        if nums[i]!=0:
            nums[i]=0
            numofwrite+=1
    print nums
    print numofwrite


nums=[0,1,0,3,12]
nums1=[0,1,0,3,12]
two_pointers(nums)
least_move(nums1)