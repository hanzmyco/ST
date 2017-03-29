# -*- coding: utf-8 -*-
'''
从后往前找第一个后面比前面大的，然后在小的那个坐标后面找第一个大过这个的
123 8 7654
 找到 3 < 8
 然后在后面找一个第一个比他大的4 12487653， reverse一下 12435678
 4 5 6 7 8 3 2 1
 4 5 6 8 7 3 2 1
 4 5 6 8 1 2 3 7
'''

def swap(a,i,j):
    temp=a[i]
    a[i]=a[j]
    a[j]=temp
def nextPermutation(nums):
    n=len(nums)
    for i in xrange(len(nums)-2,-1,-1):
        if nums[i+1] > nums[i]:
            j = n-1
            while j > i+1:
                if nums[j] > nums[i]:  #find the first one that is larger than i
                    print i
                    print j
                    break
                j-=1
            swap(nums,i,j)
            print nums
            str1=nums[i+1:]
            str1.reverse()
            nums[i+1:]=str1
            return
    nums.reverse()


nums=[1,2,7,4,3,1]
nextPermutation(nums)
print nums

