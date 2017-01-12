def validTree( n, edges):
    roots = [-1] * n
    for edge in edges:
        root1, root2 = find(roots, edge[0]), find(roots, edge[1])
        if root1 == root2:
            return False
        roots[root1] = root2
    return len(edges) == n - 1


def find(roots, vertice):
    while roots[vertice] != -1:
        vertice = roots[vertice]
    return vertice

edges=[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
validTree(5,edges)