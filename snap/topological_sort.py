def zero_Indegree(v,e,dic): #initilize
    for ite in e:
        if ite[1] not in dic:
            dic[ite[1]]=1 # the vertex that has in edge
        else:
            dic[ite[1]]+=1
    output=[]
    for ite in v:
        if ite not in dic:
            output.append(ite)
    return output

def toposort(v,e):
    dic={}
    ordered_output=[]
    zero_degree=zero_Indegree(v,e,dic)
    while zero_degree!=[]:
            ite=zero_degree[0]
            ordered_output.append(ite)
            zero_degree.remove(ite)
            delete_edge_list=[]
            for edge in e:
                if edge[0] == ite:
                    delete_edge_list.append(edge)
                    dic[edge[1]]-=1
                    if dic[edge[1]]==0:
                        zero_degree.append(edge[1])
            for ite in delete_edge_list:
                e.remove(ite)





v=['a','b','c','d','e']
e=[('a','b'),('a','d'),('b','c'),('d','c'),('d','e'),('e','c')]
toposort(v,e)
