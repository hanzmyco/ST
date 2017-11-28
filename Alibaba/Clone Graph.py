from collections import deque
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []

def cloneGraphDFS(node,dic):
    if node not in dic:
        dic[node]=UndirectedGraphNode(node.label)
        for adj in node.neighbors:
            adj_replica=cloneGraphDFS(adj,dic)
            dic[node].neighbors.append(adj_replica)
    return dic[node]

def cloneGraphBFS(node):
    if node ==None:
        return None
    que=deque()
    que.append(node)
    dic={node:UndirectedGraphNode(node.label)}
    while que:
        left=que.popleft()
        for adj in left.neighbors:
            if adj not in dic:
                dic[adj]=UndirectedGraphNode(adj.label)
                que.append(adj)
            dic[left].neighbors.append(dic[adj])
    return dic[node]




