import heapq
def cmp2(a,b):
    if a[0] < b[0]:
        return -1
    elif a[0]==b[0]:
        if a[1] <b[1]:
            return -1
        elif a[1] >b[1]:
            return 1
        else:
            if a[1]==0:
                if a[2] >b[2]:
                    return -1
                elif a[2]==b[2]:
                    return 0
                else:
                    return 1
            else:
                if a[2] > b[2]:
                    return 1
                elif a[2] == b[2]:
                    return 0
                else:
                    return -1


    else:
        return 1
def getSkyline(buildings):
    interval=[]
    for rec in buildings:
        interval.append((rec[0],0,rec[2]))
        interval.append((rec[1],1,rec[2]))
    interval.sort(cmp=cmp2)
    output=[]
    height=[]
    for ite in interval:
        if ite[1] ==0: # left point
            if len(height)==0:
                output.append((ite[0],ite[2]))
                height.append(-ite[2])
            else:
                if -ite[2] < height[0]:
                    output.append((ite[0],ite[2]))
                heapq.heappush(height,-ite[2])
        elif ite[1]==1: # right point
            if ite[2] ==-height[0]: #ite is one of the tallest
                heapq.heappop(height)
                if len(height)==0 :
                    output.append((ite[0],0))
                elif -ite[2]< height[0]:
                    output.append((ite[0],-height[0]))
            else:
                height.remove(-ite[2])
                heapq.heapify(height)
    print output

getSkyline([ [2,9 ,10], [3, 7, 15], [5, 12, 12], [15, 20 ,10], [19, 24, 8] ])
getSkyline([[0,2,3],[2,5,3]])
getSkyline([[1,2,1],[1,2,2],[1,2,3]])