# -*- coding: utf-8 -*-
'''
和union find 一样，一开始每个人的爸爸是-1，之后把后一个的爸爸赋值为前一个
最后还要确认edge数目== vertice数目-1
'''

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