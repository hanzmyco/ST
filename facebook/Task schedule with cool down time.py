import heapq
def get_time(schedule, k):
    past_time={}
    time=0
    for index,ite in enumerate(schedule):
        if ite not in past_time:
            time=max(time,index+1)

        else:
            if index - past_time[ite] <=k:
                time=max(time,past_time[ite]+k+1)
            else:
                time = max(time, index + 1)
        past_time[ite] = time
    return time

def minimal_time(schedule,k):
    total_map={}
    for ite in schedule:
        if ite not in total_map:
            total_map[ite]=1
        else:
            total_map[ite]+=1
    heap=[]
    for ite in total_map:
        heapq.heappush(heap,(-total_map[ite],ite))
    output=[]
    putback=[]
    # bug!
    while True:
        while len(heap)!=0:
            if len(putback)<k:
                item=heapq.heappop(heap)
                output.append(item[1])
                if item[0] <-1:
                    putback.append((item[0]+1,item[1]))
            else:
                heapq.heappush(heap,putback.pop(0))

        if len(putback)==0:
            break
        #for ite in putback:
        #    heapq.heappush(heap,ite)
        #putback=[]
    return output


s=[]
s.append('abbabbc')
#s.append('bb')
#s.append('aab')
for ite in s:
    print get_time(ite,3)
    print minimal_time(ite,3)
    print get_time(minimal_time(ite, 3),3)


