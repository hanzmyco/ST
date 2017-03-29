# -*- coding: utf-8 -*-
'''
拓扑排序 两个字典，一个存每个节点的入度，一个存每个节点的出节点，对于入度为0的节点，找到它的所有出节点，把那些出度为0的节点再次做
同样操作
'''


from collections import deque
def build_graph(words):
    edges={}
    vertice=set()
    in_degree={}

    for index in xrange(0,len(words)-1):
        flag=0
        minn=min(len(words[index]),len(words[index+1]))
        for i in xrange(0,minn):
            if flag==0 and words[index][i] !=words[index+1][i]:
                if words[index][i] not in edges:
                    edges[words[index][i]]=[words[index+1][i]]
                else:
                    edges[words[index][i]].append(words[index+1][i])
                if words[index + 1][i] not in in_degree:
                    in_degree[words[index+1][i]]=1
                else:
                    in_degree[words[index + 1][i]] += 1

                flag=1
            vertice.add(words[index][i])
            vertice.add(words[index+1][i])
        if len(words[index]) > minn:
            for i in xrange(minn,len(words[index])):
                vertice.add(words[index][i])
        elif len(words[index+1]) > minn:
            for i in xrange(minn,len(words[index+1])):
                vertice.add(words[index+1][i])

    return edges,vertice, in_degree

def alienOrder(words):
    if len(words) == 1:
        return words[0]
    edges, vertice, in_degree= build_graph(words)

    # avoid corner cases
    if len(edges) == 0 and len(in_degree) == 0:
        if len(vertice) == 1:
            return words[0][0]
        else:
            i = 0
            while i + 1 < len(words):
                if len(words[i]) > len(words[i + 1]):   # 出现问题
                    return ''
                i += 1



    output=''
    que=deque()
    for ite in vertice:
        if ite not in in_degree:
            que.append(ite)
    while len(que)!=0:
        ite=que.popleft()
        output+=ite
        if ite in edges:
            for out_node in edges[ite]:
                if in_degree[out_node]==1:
                    del in_degree[out_node]
                    que.append(out_node)
                else:
                    in_degree[out_node]-=1
    # avoid loop
    if len(in_degree)!=0:
        return ''
    return output

words=["wrt","wrf","er","ett","rftt"]
words1=['wrt','wrtkj']
words2=['wnlb']
print alienOrder(words2)