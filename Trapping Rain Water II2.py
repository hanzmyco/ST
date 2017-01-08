def check(i,j,m,n,heightMap,trap):
    if heightMap[i-1][j]<=heightMap[i][j]:
        if trap[i-1][j]==-1: # up cannot trap
            trap[i][j]=-1
            return
        elif 


def trapRainWater(self, heightMap):
    """
    :type heightMap: List[List[int]]
    :rtype: int
    """
    m=len(heightmap)
    if m!=0:
        n=len(heightmap[0])
    trap=[]
    # trap[i]==-1  means cannot trap
    trap.append([])
    for j in xrange(0,n):
        trap[0].append(-1)

    for i in xrange(1,m):
        trap.append([])
        for j in xrange(0,n):
            if j!=0:
                trap[i].append(-2)
            else:
                trap[i].append(-1)
    count=1
    while count*2<m and count*2 <n:
        for i in xrange(count,n-count):
            check(count,i,m,n,heightmap,trap)
        for i in xrange(count+1,m-count):
            check(i,n-count-1,m,n,heightmap,trap)
        if (m-2*count==1 or n-2*count==1):
            break
        i=n-count-2
        while i>=count:
            check(m-count-1,i,m,n,heightmap,trap)
            i-=1
        i=m-count-2
        while i>=count+1:
            check(i,count,m,n,heightmap,trap)
            i-=1
        count+=1
