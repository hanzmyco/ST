# -*- coding: utf-8 -*-
'''
resiervir sampling
如果nums[i]==target，就增加cnt，然后从（0，cnt-1）random的选一个，如果是0，那么就把res更新为nums[i]
'''

def random_pick(nums,target):
    li=[]
    cnt=0
    res=-1
    for ite in nums:
        if ite !=target:
            continue
        cnt+=1
        if random.randint(0,cnt-1)==0:
            res=ite
    return res