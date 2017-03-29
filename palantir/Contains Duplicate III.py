# -*- coding: utf-8 -*-
'''
桶排序

'''

def containsNearbyAlmostDuplicate(self, nums, k, t):
    base=-10000
    if k <1 or t<0:
        return False
    map={}
    for i in xrange(0,len(nums)):
        abs_num=nums[i]-base
        bucket=abs_num/(t+1)
        if bucket in map or (bucket-1 in map and abs_num-map[bucket-1]<=t) or (bucket+1 in map and -abs_num+map[bucket+1]<=t):
            return True
        if len(map)>=k:
            lastbucket=(nums[i-k]-base)/(t+1)
            del map[lastbucket]
        map[bucket]=abs_num
    return False

