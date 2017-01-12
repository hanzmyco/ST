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
    num_sche=len(schedule)
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

    while len(heap)!=0 or len(putback)!=0:
        if len(putback)<=k and len(heap)!=0:
            item=heapq.heappop(heap)
            output.append(item[1])
            num_sche-=1
            if num_sche==0:
                break
            putback.append((item[0],item[1]))
        else: # you should
            while len(heap)==0 and len(putback)<=k:  # we can use nothing now, since everything is in the window
                output.append('')
                putback.append('')
            if len(putback)>k:    # now we can put back the head if it is valid
                head=putback.pop(0)
                if head !='' and head[0]<-1:
                    heapq.heappush(heap,(head[0]+1,head[1]))

    print output
    print len(output)

def minimal_time2(schedule,k):
    total_map = {}
    num_sche = len(schedule)
    for ite in schedule:
        if ite not in total_map:
            total_map[ite] = 1
        else:
            total_map[ite] += 1
    heap = []
    for ite in total_map:
        heapq.heappush(heap, (-total_map[ite], ite))
    output = []
    start=0
    end=0
    print end-len(output)
    while len(heap) != 0 or len(total_map) != 0:
        if len(output)-start <= k and len(heap) != 0:
            item = heapq.heappop(heap)
            output.append(item[1])
            num_sche -= 1
            if num_sche == 0:
                break
            end+=1
            if item[0]==-1:
                del total_map[item[1]]

            else:
                total_map[item[1]]-=1
        else:  # you should
            while len(heap) == 0 and end-start <= k:  # we can use nothing now, since everything is in the window
                output.append('')
                end+=1
            if len(output)-start > k:  # now the window size is larger than k
                head = output[start]
                start+=1
                if head != '' and head in total_map:
                    heapq.heappush(heap, (-total_map[head] , head))

    print output
    #print len(output)

s=[]
s.append('abbabbc')
s.append('abbacbcd')
s.append('aab')
s.append('abcdefg')
for ite in s:
    #print get_time(ite,3)
    minimal_time(ite,3)
    minimal_time2(ite,3)
