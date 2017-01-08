import heapq
import copy



def dfs2(cur,output,dic,box,l,dic2):
    output.append(cur)
    if len(output)==l:
        box.append(copy.deepcopy(output))
    if cur in dic:
        for ite in dic[cur]:
            if dic2[(cur,ite)]>0:
                dic2[(cur,ite)]-=1
                dfs2(ite,output,dic,box,l,dic2)
                dic2[(cur, ite)] += 1
    output.pop()
    return


def main2(tickets):
    dic={}
    dic2={}
    for ite in tickets:
        if ite[0] not in dic:
            dic[ite[0]]=[ite[1]]
            dic2[(ite[0],ite[1])]=1
        else:
            dic[ite[0]].append(ite[1])
            if (ite[0],ite[1]) in dic2:
                dic2[(ite[0],ite[1])]+=1
            else:
                dic2[(ite[0], ite[1])] = 1

    l=len(tickets)
    output=[]
    box=[]
    dfs2('a',output,dic,box,l+1,dic2)
    print box

def dfs(cur,output,dic):
    while cur in dic and len(dic[cur])!=0:
        dfs(heapq.heappop(dic[cur]),output,dic)
    output.append(cur)

def main(tickets):
    dic = {}
    for ite in tickets:
        if ite[0] not in dic:
            heap = []
            heapq.heappush(heap, ite[1])
            dic[ite[0]] = heap
        else:
            heapq.heappush(dic[ite[0]], ite[1])
    output = []
    dfs('JFK', output, dic)
    output.reverse()
    print output

tickets1=[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets=[['a','b'],['a','c'],['c','a']]
main(tickets1)
main2(tickets)
