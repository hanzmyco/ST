# -*- coding: utf-8 -*-
'''

'''
class topo_sort(object):
    def __init__(self, nodes, root, target):
        self.nodes = nodes
        self.root = root
        self.target = target
        self.sub_graph = set()  # every node is reachable
        self.visited = set()

    def dfs(self, node1, node2):
        tag = False
        for child in self.nodes[node1]:
            if child == node2 or child in self.sub_graph: #child is accebile to then node1 is also accebile to
                self.sub_graph.add(node1)
                tag=True
            elif child not in self.visited:
                tag=tag or self.dfs(child,node2)
        if not tag:
            self.visited.add(node1)
        return tag


    # self.sub_graph 有了所有可以reachable 到C的点
    def topo_sort(self):
        self.dfs(self.root, self.target)
        # the others are just topo sort

