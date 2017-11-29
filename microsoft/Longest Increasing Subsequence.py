# -*- coding: utf-8 -*-

'''
找第一个比位置前一个比ite小后一个比ite大，然后就把后面那一个变成ite
'''


def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums)==0:
        return 0
    res=[nums[0]]
    l=0
    for ite in nums:
           left=0
           right=l
           while left<right:
               mid=left+(right-left)/2
               if res[mid]<ite:
                   left=mid+1
               else:
                   right=mid

           if right>=l:
               res.append(ite)
               l+=1
           else:
            res[right]=ite
    return l