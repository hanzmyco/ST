# -*- coding: utf-8 -*-
'''

'''
from collections import deque
def bfs(grid):
    que=deque()
    dic={}
    m=len(grid)
    n=0
    if m>0:
       n=len(grid[0])
    num=0
    for i in xrange(0,m):
        for j in xrange(0,n):
            if grid[i][j]=='1' and (i,j) not in dic:
                num+=1
                que.append((i,j))
                dic[(i,j)]=1
                while len(que)!=0:
                    top=que.popleft()
                    x=top[0]
                    y=top[1]
                    if x>0 and grid[x-1][y]=='1' and (x-1,y) not in dic:
                        dic[(x-1,y)]=1
                        que.append((x-1,y))
                    if x < m-1 and grid[x + 1][y] == '1' and (x + 1, y) not in dic:
                        dic[(x + 1, y)] = 1
                        que.append((x + 1, y))
                    if y > 0 and grid[x][y-1] == '1' and (x, y-1) not in dic:
                        dic[(x, y-1)] = 1
                        que.append((x, y-1))
                    if y < n-1 and grid[x][y+1] == '1' and (x, y+1) not in dic:
                        dic[(x, y+1)] = 1
                        que.append((x, y+1))
    return num


def dfs_norecur(grid):
    stack=[]
    num=0
    m=len(grid)
    n=0
    if m>0:
        n=len(grid[0])
    dic={}
    for x in xrange(0,m):
        for y in xrange(0,n):
            if grid[x][y]=='1' and (x,y) not in dic:
                num+=1
                stack.append((x,y))
                while len(stack)!=0:
                    top=stack[len(stack)-1]
                    i=top[0]
                    j=top[1]
                    if (i,j) not in dic:
                        dic[(i, j)] = 1
                    if i > 0:
                        if grid[i - 1][j] == '1' and (i - 1, j) not in dic:
                            stack.append((i - 1, j))
                            continue
                    if i < m-1:
                        if grid[i + 1][j] == '1' and (i + 1, j) not in dic:
                            stack.append((i + 1, j))
                            continue
                    if j > 0:
                        if grid[i][j - 1] == '1' and (i, j - 1) not in dic:
                            stack.append((i, j - 1))
                            continue
                    if j < n-1:
                        if grid[i][j + 1] == '1' and (i, j + 1) not in dic:
                            stack.append((i, j + 1))
                            continue
                    stack.pop()
    return num

def recur(grid, i, j, dic):
        dic[(i, j)] = 1
        if i > 0:
            if grid[i - 1][j] == '1' and (i - 1, j) not in dic:
                recur(grid, i - 1, j, dic)
        if i < len(grid) - 1:
            if grid[i + 1][j] == '1' and (i + 1, j) not in dic:
                recur(grid, i + 1, j, dic)
        if j > 0:
            if grid[i][j - 1] == '1' and (i, j - 1) not in dic:
                recur(grid, i, j - 1, dic)
        if j < len(grid[0]) - 1:
            if grid[i][j + 1] == '1' and (i, j + 1) not in dic:
                recur(grid, i, j + 1, dic)
def dfs(grid):
    num = 0
    m = len(grid)
    n = 0
    if m > 0:
        n = len(grid[0])
    dic = {}
    for i in xrange(0, m):
        for j in xrange(0, n):
            if grid[i][j] == '1' and (i, j) not in dic:
                num += 1
                recur(grid, i, j, dic)
    return num
def twoD2oneD(n,r,c):
    return r*n+c

# check the number of unique shape island
def followup(grid):
    que=deque()
    dic={}
    m=len(grid)
    n=0
    if m>0:
       n=len(grid[0])
    num=0
    vectors=set()
    for i in xrange(0,m):
        for j in xrange(0,n):
            if grid[i][j]=='1' and (i,j) not in dic:
                points=[]
                low_r=i
                low_c=j
                que.append((i,j))
                points.append((i,j))
                dic[(i, j)] = 1
                while len(que)!=0:
                    top=que.popleft()
                    x=top[0]
                    y=top[1]
                    if x>0 and grid[x-1][y]=='1' and (x-1,y) not in dic:
                        dic[(x-1,y)]=1
                        low_r=min(low_r,x-1)
                        points.append((x-1,y))
                        que.append((x-1,y))
                    if x < m-1 and grid[x + 1][y] == '1' and (x + 1, y) not in dic:
                        dic[(x + 1, y)] = 1
                        que.append((x + 1, y))
                        points.append((x+1,y))
                    if y > 0 and grid[x][y-1] == '1' and (x, y-1) not in dic:
                        dic[(x, y-1)] = 1
                        que.append((x, y-1))
                        low_c=min(low_c,y-1)
                        points.append((x,y-1))
                    if y < n-1 and grid[x][y+1] == '1' and (x, y+1) not in dic:
                        dic[(x, y+1)] = 1
                        que.append((x, y+1))
                        points.append((x,y+1))
                vector=[]
                for point in points:
                    vector.append(n*(point[0]-low_r)+point[1]-low_c)
                vector.sort()
                vectors.add(tuple(vector))

    return len(vectors)

o='1'
z='0'
#grid=[[o,o,z,z,z],[o,o,z,z,z],[z,z,o,z,z],[z,z,z,o,o]]
#grid=[[o,o,o,o,z],[o,o,z,o,z],[o,o,z,z,z],[z,z,z,z,z]]
grid=[[o,o,z,z,z,z],[o,o,z,z,z,o],[z,z,o,o,z,o],[o,z,o,o,z,z],[o,z,z,z,z,z]]

print bfs(grid)
print dfs_norecur(grid)
print followup(grid)