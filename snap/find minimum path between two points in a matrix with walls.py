import heapq

def bfs(x,y,m,n,grid,que,dic):
    if x > 0 and (x-1,y) not in dic and grid[x-1][y]>=0:
        grid[x-1][y]+=grid[x][y]
        heapq.heappush(que, (grid[x - 1][y], x - 1, y))
        dic[(x-1,y)]=1
    if x < m - 1 and (x+1,y) not in dic and grid[x+1][y]>=0:
        grid[x + 1][y] += grid[x][y]
        heapq.heappush(que, (grid[x + 1][y], x + 1, y))
        dic[(x+1,y)]=1
    if y > 0 and (x,y-1) not in dic and grid[x][y-1]>=0:
        grid[x][y-1] += grid[x][y]
        heapq.heappush(que, (grid[x][y - 1], x, y - 1))
        dic[(x,y-1)]=1
    if y < n - 1 and (x,y+1) not in dic and grid[x][y+1]>=0:
        grid[x][y+1] += grid[x][y]
        heapq.heappush(que, (grid[x][y + 1], x, y + 1))
        dic[(x,y+1)]=1

def maze_bfs(grid,start,end):
    x=start[0]
    y=start[1]
    que=[]
    m=len(grid)
    n=len(grid[0])
    dic={}
    dic[(x,y)]=1
    bfs(x,y,m,n,grid,que,dic)
    while len(que) !=0:
        top=heapq.heappop(que)
        if top[1]==end[0] and top[2] ==end[1]:
            print grid[end[0]][end[1]]
            break
        bfs(top[1],top[2],m,n,grid,que,dic)



grid=[[0,2,2],[1,-3,1],[1,4,0]]
maze_bfs(grid,(0,0),(2,2))
