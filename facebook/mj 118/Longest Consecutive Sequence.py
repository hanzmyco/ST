class union_find(object):
    def __init(self):
        self.parent = {}
        self.numofTree = {}

    def insert(self, a):
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
        numa = self.numofTree(roota)
        numb = self.numofTree(rootb)
        if roota >= rootb:
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
        return self.numofTree(self.findroot(a))