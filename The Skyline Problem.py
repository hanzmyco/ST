import heapq
def cmp1(a,b):
    if a[0]!=b[0]:
        return  a[0]-b[0]
    elif a[1]<0 and b[1]<0:
        return a[1]-b[1]
    elif a[1]>0 and b[1]>0:
        return a[1]-b[1]
    else:
        return a[1]
def getSkyline(buildings):
    """
    :type buildings: List[List[int]]
    :rtype: List[List[int]]
    """
    height=[]
    for ite in buildings:
        height.append((ite[0],-ite[2]))
        height.append((ite[1],ite[2]))
    #print height
    #height=sorted(height,cmp=cmp1)
    height.sort(cmp=cmp1)
    #print height
    heap=[0]
    pre=0
    cur=0
    output=[]
    for ite in height:
        if ite[1]<0:
            heapq.heappush(heap,ite[1])
        else:
            heap.remove(-ite[1])
            heapq.heapify(heap)
        cur=min(heap)
        if pre!=cur:
            output.append((ite[0],-cur))
            pre=cur
    return output


buildings=[[2,9,10], [3,7,15],[5,12,12], [15,20,10], [19,24,8]]
print getSkyline(buildings)
