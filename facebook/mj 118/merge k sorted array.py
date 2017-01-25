import heapq
def merge_k_sorted_array(arrays,last_index):
    l=len(arrays)
    if l==0:
        return None
    if l==1:
        return arrays[0]
    last=l-1
    heap=[]
    len_list=[]
    for index,ite in enumerate(arrays):
        if index != len(arrays)-1:
            len_list.append(len(ite)-1)
            heapq.heappush(heap,(-ite[len(ite)-1],index))
        else:
            len_list.append(last_index)
            heapq.heappush(heap,(-ite[last_index],len(arrays)-1))
    position=len(arrays[last])-1
    num=l-1
    while len(heap)!=0 and num>0:
        top=heapq.heappop(heap)
        len_list[top[1]]-=1
        arrays[last][position]=-top[0]
        position-=1
        if len_list[top[1]]>=0:
            heapq.heappush(heap,(-arrays[top[1]][len_list[top[1]]],top[1]))
        else:
            num-=1
    if num==0:
        for index,leng in enumerate(len_list):
            if leng!=-1:
                arrays[last][0:position+1]=arrays[index][0:leng+1]

    print arrays[last]

arrays=[[1,2,7],[3,5],[4,6,0,0,0,0,0]]
merge_k_sorted_array(arrays,1)
