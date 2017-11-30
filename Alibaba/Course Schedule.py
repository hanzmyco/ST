from collections import deque


def out_dic(prere,output_dic,degree_dic):
    for edge in prere:
        if edge[1] not in output_dic:
            output_dic[edge[1]]=[]
        output_dic[edge[1]].append(edge[0])
        if edge[0] not in degree_dic:
            degree_dic[edge[0]]=1
        else:
            degree_dic[edge[0]]+=1
        if edge[1] not in degree_dic:
            degree_dic[edge[1]] = 0



def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    out_edges={}
    degree_dic={}
    out_dic(prerequisites,out_edges,degree_dic)
    que=deque()
    for i in range(0,numCourses):
        if i not in degree_dic or degree_dic[i]==0:
            que.append(i)
    if len(que)==0:
        return False
    cal_num=len(que)
    while len(que)!=0:
        prere=que.popleft()
        if prere in out_edges:
            for next in out_edges[prere]:
                degree_dic[next]-=1
                if degree_dic[next]==0:
                    que.append(next)
                    cal_num+=1
    if cal_num!=numCourses:
        return False
    return True

print(canFinish(3,[[1,0]]))