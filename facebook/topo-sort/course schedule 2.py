# -*- coding: utf-8 -*-
'''
topo logistic sort
'''

from collections import deque
def build_topo(prerequisites):
    in_degree={}
    children={}
    for ite in prerequisites:
        if ite[0] not in in_degree:
            in_degree[ite[0]]=1
        else:
            in_degree[ite[0]]+=1
        if ite[1] not in children:
            children[ite[1]]=[ite[0]]
        else:
            children[ite[1]].append(ite[0])
    return in_degree, children


def findOrder(numCourses, prerequisites):
    in_degree,children=build_topo(prerequisites)
    output=[]
    for i in xrange(0,numCourses):
        if i not in in_degree and i not in children:
            output.append(i)

    que=deque()
    for ite in children:
        if ite not in in_degree:
            que.append(ite)
    while len(que)!=0:
        head=que.popleft()
        output.append(head)
        if head in children:
            for out_node in children[head]:
                if in_degree[out_node]==1:
                    que.append(out_node)
                    del in_degree[out_node]
                else:
                    in_degree[out_node]-=1
    if len(in_degree)!=0:
        return []
    return output
numC=4
prerequisites=[[1,0],[2,0],[3,1],[3,2]]
print findOrder(numC,prerequisites)
numC=2
prerequisites=[[1,0],[0,1]]
print findOrder(numC,prerequisites)
