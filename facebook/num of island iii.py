def add_adjacent(root,stack,grid,dic,m,n):
    i=root[0]
    j=root[1]
    if i>0:
        if grid[i-1][j]=='1' and (i-1,j) not in dic:
            root[2][0]+=1
            stack.append([i-1,j,root[2]])
            dic[(i-1,j)]=1
    if i<m:
        if grid[i+1][j]=='1' and (i+1,j) not in dic:
            root[2][0]+=1
            stack.append([i+1,j,root[2]])
            dic[(i+1,j)]=1
    if j>0:
        if grid[i][j-1]=='1' and (i,j-1) not in dic:
            root[2][0]+=1
            stack.append([i,j-1,root[2]])
            dic[(i,j-1)]=1
    if j<n:
        if grid[i][j+1]=='1' and (i,j+1) not in dic:
            root[2][0]+=1
            stack.append([i,j+1,root[2]])
            dic[(i,j+1)]=1


def maxIsland(grid):
     stack=[]
     dic={}
     m=len(grid)
     n=0
     if m!=0:
         n=len(grid[0])
     max_num=0
     for i in xrange(0,m):
         for j in xrange(0,n):
             if grid[i][j]=='1' and (i,j) not in dic:
                 num=[1]
                 stack.append([i,j,num])
                 dic[(i,j)]=1
                 while (len(stack))!=0:
                     root=stack.pop()
                     add_adjacent(root,stack,grid,dic,m,n)
                 max_num=max(max_num,num[0])
     return max_num

o='1'
z='0'
grid=[[o,o,z,z,z],[o,o,z,z,z],[z,z,o,z,z],[z,z,z,1,1]]
print maxIsland(grid)



