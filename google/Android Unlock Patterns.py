# -*- coding: utf-8 -*-
'''
不相邻的肯定会之后才访问到，所以不用考虑, 1 3 9 7 对称，2,4 6 8

'''

def dfs(vis,skip,cur,remain):
    if remain ==0:
        return 1
    vis[cur]=True
    rst=0
    for i in xrange(1,10):
        if not vis[i] and (skip[cur][i]==0 or vis[skip[cur][i]]):
            rst+=dfs(vis,skip,i,remain-1)
    vis[cur]=False
    return rst

def numberOfPatterns(m, n):
    skip=[]
    for i in xrange(0,10):
        skip.append([0]*10)
    skip[1][3] = skip[3][1] = 2
    skip[1][7] = skip[7][1] = 4
    skip[3][9] = skip[9][3] = 6
    skip[7][9] = skip[9][7] = 8
    skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] =5
    vis=[False]*10
    rst=0
    for i in xrange(m,n+1):
        rst+=dfs(vis,skip,1,i-1)*4
        rst += dfs(vis, skip, 2, i - 1) * 4
        rst += dfs(vis, skip, 5, i - 1)
    return rst


numberOfPatterns(0,0)