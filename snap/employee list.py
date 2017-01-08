def que_iterate(root):
    output=[]
    que=[root]
    while len(que)!=0:
        output.append(que[0])
        father=que.pop(0)
        if father in dic:
            for child in dic[father]:
                que.append(child)
    return output

def dfs(root,output):
    output.append(root)
    if root in dic:
        for i in dic[root]:
            dfs(i,output)

input1=[(1,2),(0,0),(2,0),(3,0),(4,4),(6,7),(5,5),(7,5),(8,5)]

dic={}
dic1={}
for ite in input1:
    child=ite[0]
    father=ite[1]
    if child != father:
        if father not in dic:
            dic[father]=[child]
        else:
            dic[father].append(child)
        dic1[child]=father
    else:
        dic1[child]=-1
self_employed=[]
roots=[]
for ite in input1:
    if dic1[ite[0]]==-1:
        if ite[0] not in dic:
            self_employed.append(ite[0])
        else:
            roots.append(ite[0])
for ite in roots:
    output=[]
    dfs(ite,output)
    print output

for ite in self_employed:
    print ite
