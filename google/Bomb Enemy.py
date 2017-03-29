# -*- coding: utf-8 -*-
'''
rowhit只要一个变量是因为按列走，每一行的rowhit只会连续存在
colhit要一个数组，因为每一列的colhit会重复被访问，而且有可能会被更新，
关键是看看上一个值是不是墙，如果是墙就要更新
'''

def maxKilledEnemies(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    m = len(grid)
    n = 0
    if m != 0:
        n = len(grid[0])
    rowhits, colhits = 0, [0] * n
    res=0
    for i in xrange(0, m):
        for j in xrange(0, n):
            if j == 0 or grid[i][j - 1] == 'W':
                rowhits = 0
                k = j
                while k < n and grid[i][k] != 'W':
                    if grid[i][k] == 'E':
                        rowhits += 1
                    k+=1
            if i==0 or grid[i-1][j]=='W':
                colhits[j]=0
                k=i
                while k<m and grid[k][j]!='W':
                    if grid[k][j]=='E':
                        colhits[j]+=1
                    k+=1
            if grid[i][j]=='0':
                res=max(res,rowhits+colhits[j])
    return res

