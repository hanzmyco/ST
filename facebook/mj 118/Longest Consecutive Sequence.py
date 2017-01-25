class union_find(object):
    def __init__(self):
        self.parent = {}
        self.numofTree = {}

    def get_numofTree(self):
        return self.numofTree
    def insert(self, a):
        if a not in self.parent:
            self.parent.setdefault(a, a)
            self.numofTree.setdefault(a, 1)
            self.createTree(a)

    def findroot(self, a):
        parent = self.parent[a]
        if parent in self.numofTree:
            return parent
        else:
            return self.findroot(parent)

    def union(self, a, b):
        roota = self.findroot(a)
        rootb = self.findroot(b)
        numa = self.numofTree[roota]
        numb = self.numofTree[rootb]
        if numa >= numb:
            del self.numofTree[rootb]
            self.numofTree[roota] += numb
            self.parent[rootb] = roota
        else:
            del self.numofTree[roota]
            self.numofTree[rootb] += numa
            self.parent[roota] = rootb

    def createTree(self, a):
        if a + 1 in self.parent and self.findroot(a) != self.findroot(a + 1):
            self.union(a, a + 1)
        if a - 1 in self.parent and self.findroot(a) != self.findroot(a - 1):
            self.union(a, a - 1)
        return self.numofTree[self.findroot(a)]

nums=[100,4,200,1,3,2]
nums=[0,3,7,2,5,8,4,6,0,1]
nums=[-3,2,8,5,1,7,-8,2,-8,-4,-1,6,-6,9,6,0,-7,4,5,-4,8,2,0,-2,-6,9,-4,-1]
u=union_find()
res=0
for i in nums:
    print i
    u.insert(i)
    res = max(res, u.numofTree[u.findroot(i)])
print res
