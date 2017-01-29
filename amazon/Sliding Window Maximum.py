# -*- coding: utf-8 -*-
'''
如果最左边已经等于i-k,那么就把这个删掉
如果最右边的值比当前值小，那么就把最右边抛出来

'''

from collections import deque
def maxSlidingWindow(nums, k):
    res=[]
    que=deque()
    for i in xrange(0,len(nums)):
        if len(que)!=0 and que[0]==i-k:
            que.popleft()
        while len(que)>0 and que[len(que)-1] <nums[i]:
            que.pop()
        que.append(i)
        if i>=k-1:
            res.append(que[0])
    return res

