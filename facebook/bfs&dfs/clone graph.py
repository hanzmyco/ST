# -*- coding: utf-8 -*-
'''

'''

def dfs(self, node, dic):
    if node == None:
        return node
    if node.label in dic:
        return dic[node.label]
    new_node = UndirectedGraphNode(node.label)
    dic[node.label] = new_node
    for ite in node.neighbors:
        new_node.neighbors.append(self.dfs(ite, dic))
    return new_node

def bfs(node):
    if node == None:
        return None
    map = {node.label: UndirectedGraphNode(node.label)}
    que = collections.deque()
    que.append(node)

    while len(que) != 0:
        top = que.popleft()
        new_node = map[top.label]
        for ite in top.neighbors:
            if ite.label not in map:
                map[ite.label] = UndirectedGraphNode(ite.label)
                que.append(ite)
            new_node.neighbors.append(map[ite.label])

    return map[node.label]