# -*- coding: utf-8 -*-
'''
bfs要记录上下两层的个数，上一层个数为0时，层数+1，num_first_layer=num_second,
second=0
dfs_iteration要麻烦一点，stack存一个当前的list，当前的长度，当前用到哪个i，反正就是模仿dfs_recur
'''
import copy
from collections import deque


def dfs(i, output, k, current, n):
    if k > 1:
        current.append(i)
        for j in xrange(i + 1, n + 1):
            dfs(j, output, k - 1, current, n)
        current.pop()
    elif k == 1:
        current.append(i)
        output.append(copy.deepcopy(current))
        current.pop()


def dfs_ite(n,k):
    stack=[]
    l=0
    for i in xrange(n-k+1,0,-1):
        stack.append(([i], 1, i))
        l += 1

    output=[]
    while l!=0:
        top=stack.pop()
        l-=1
        if top[1]==k-1:
            if top[2] < n:
                top[0].append(top[2]+1)
                output.append(copy.deepcopy(top[0]))
                top[0].pop()
                if top[2] !=n-1:
                    stack.append((top[0],top[1],top[2]+1))
                    l+=1
        else:
            if top[2]<n:
                stack.append((top[0],top[1],top[2]+1))
                l+=1
                new_com=copy.deepcopy(top[0])
                new_com.append(top[2]+1)
                stack.append((new_com,top[1]+1,top[2]+1))
                l+=1
    print output






def bfs(n,k):
    que=deque()
    first_layer_l=n-k+1
    second_layer_l=0
    l=0
    for i in xrange(1,n-k+2):
        que.append([i])
        l+=1
    if k==1:
        print que
        return
    output=[]
    layer=1
    while l!=0:
        top=que.popleft()
        l-=1
        first_layer_l-=1
        for i in xrange(top[len(top)-1]+1,n+1):
            top.append(i)
            second_layer_l+=1
            temp_comb=copy.deepcopy(top)
            if layer==k-1:
                output.append(temp_comb)
            else:
                que.append(temp_comb)
                l+=1
            top.pop()
        if first_layer_l==0: #上一层搞完了
            first_layer_l=second_layer_l
            second_layer_l=0
            layer+=1
    print output


def combine(n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        output = []
        current=[]
        for i in xrange(1, n + 1):
            dfs(i, output, k,current,n)

        print output

combine(5,2)
bfs(5,2)
dfs_ite(5,2)