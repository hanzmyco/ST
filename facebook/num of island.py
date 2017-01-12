def dfs_norecur(grid):
    stack1=[]
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
                stack1.append((x,y))
                dic[(x,y)]=1
                while len(stack1)!=0:
                    top=stack1.pop()
                    i=top[0]
                    j=top[1]
                    if i > 0:
                        if grid[i - 1][j] == '1' and (i - 1, j) not in dic:
                            stack1.append((i - 1, j))
                            dic[(i - 1, j)] = 1
                    if i < m:
                        if grid[i + 1][j] == '1' and (i + 1, j) not in dic:
                            stack1.append((i + 1, j))
                            dic[(i + 1, j)] = 1
                    if j > 0:
                        if grid[i][j - 1] == '1' and (i, j - 1) not in dic:
                            stack1.append((i, j - 1))
                            dic[(i, j - 1)] = 1
                    if j < n:
                        if grid[i][j + 1] == '1' and (i, j + 1) not in dic:
                            stack1.append((i, j + 1))
                            dic[(i, j + 1)] = 1

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