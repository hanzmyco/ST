from collections import deque
class deadlock(object):
    # dependency is a set of edges like (1,2) means node1 is depending on node2
    def __init__(self, dependency):
        self.thread_list=set()
        self.in_degree={}
        self.thread_graph={}
        for edge in dependency:
            if edge[0] not in self.thread_list:
                self.thread_list.add(edge[0])
            if edge[1] not in self.thread_list:
                self.thread_list.add(edge[1])
            if edge[1] not in self.in_degree:
                self.in_degree[edge[1]]=1
            else:
                self.in_degree[edge[1]]+=1
            if edge[0] not in self.thread_graph:
                self.thread_graph[edge[0]]=[edge[1]]
            else:
                self.thread_graph[edge[0]].append(edge[1])
    def topo_sort(self):
        zero_degree=deque()
        for node in self.thread_list:
            if node not in self.in_degree:
                zero_degree.append(node)
        while len(zero_degree)!=0:
            node=zero_degree.popleft()
            for out_node in self.thread_graph[node]:
                if self.in_degree[out_node]>1:
                    self.in_degree[out_node]-=1
                else:
                    del self.in_degree[out_node]
                    zero_degree.append(out_node)
            del self.thread_graph[node]
        return len(self.in_degree) # number of thread which generate the deadlock

