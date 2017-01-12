# two factors: 1. whether every node is linked with each other
# 2. if each node is linked with each other in one path


def validTree(n,edges):
    roots=[-1]*n
    for edge in edges:
        root1,root2=find(roots,edge[0]),find(roots,edge[1])
        if root1==root2:
            return False
        roots[root1]=root2
    return len(edges)==n-1
def find(roots,vertice):
    while roots[vertice]!=-1:
        vertice=roots[vertice]
    return vertice
