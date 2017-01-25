import heapq

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
