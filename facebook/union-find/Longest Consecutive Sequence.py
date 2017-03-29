# -*- coding: utf-8 -*-
'''
典型的union find题目，可以考虑路径压缩法，即每个节点只存他真正的root是谁，而不是把所有root接起来

'''

class union_find(object):
    def __init__(self):
        self.parent = {}
        self.children = {}


    #def get_numofTree(self):
    #    return self.numofTree
    def insert(self, a):
        if a not in self.parent:
            self.parent.setdefault(a, a)
            self.children.setdefault(a, [a])
            self.createTree(a)

    #def findroot(self, a):
     #   return self.parent[a]
        #if parent in self.numofTree:
         #   return parent
        #else:
         #   return self.findroot(parent)

    def union(self, a, b):
        roota = self.parent[a]
        rootb = self.parent[b]
        numa = len(self.children[roota])
        numb = len(self.children[rootb])
        if numa > numb or (numa==numb and a<b):
            for child in self.children[rootb]:
                self.parent[child]=roota
                self.children[roota].append(child)
            del self.children[rootb]
        elif numa<numb or (numa==numb and a>b):
            for child in self.children[roota]:
                self.parent[child]=rootb
                self.children[rootb].append(child)
            del self.children[roota]

    def createTree(self, a):
        if a - 1 in self.parent:
            self.union(a, a - 1)
        
        if a + 1 in self.parent:
            self.union(a, a + 1)
        return len(self.children[self.parent[a]])

nums=[100,4,200,1,3,2]
nums=[0,3,7,2,5,8,4,6,0,1]
nums=[-3,2,8,5,1,7,-8,2,-8,-4,-1,6,-6,9,6,0,-7,4,5,-4,8,2,0,-2,-6,9,-4,-1]
u=union_find()
res=0
for i in nums:
    #print i
    u.insert(i)
    res = max(res, len(u.children[u.parent[i]]))
print res
