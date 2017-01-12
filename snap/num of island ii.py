class unionfind():
    def __init__(self,position):
        self.position=position
        self.parent={}
        self.numofTree={}  # only store root


    def insert(self,a):
        self.parent.setdefault(a,a)
        self.numofTree.setdefault(a,1)
        self.createTree(a)
        self.position[a[0]][a[1]]=1

    def createTree(self,a):  # union its adjacent node
        if a[0]>0:
            b=(a[0]-1,a[1])
            if self.position[b[0]][b[1]] ==1:
               if  self.findroot(a) !=self.findroot(b):
                   self.union(b,a)
        if a[0]<len(self.position)-1:
            b=(a[0]+1,a[1])
            if self.position[b[0]][b[1]] ==1:
                if self.findroot(a) !=self.findroot(b):
                    self.union(b,a)
        if a[1] >0:
            b = (a[0], a[1]-1)
            if self.position[b[0]][b[1]] == 1:
                if self.findroot(a) != self.findroot(b):
                    self.union(b, a)
        if a[1] < len(self.position[0]) -1:
            b=(a[0],a[1]+1)
            if self.position[b[0]][b[1]] == 1:
                if self.findroot(a) != self.findroot(b):
                    self.union(b, a)


    def findroot(self,a):      # can make every node point to the root
        parent=self.parent[a]
        if  parent in self.numofTree:
            return parent
        else:
            return self.findroot(parent)

    def union(self,a,b):
        roota=self.findroot(a)
        rootb=self.findroot(b)
        num1=self.numofTree[roota]
        num2=self.numofTree[rootb]
        if num1>=num2:
            self.numofTree[roota]+=num2
            self.numofTree.pop(rootb)
            self.parent[rootb]=roota
        else:
            self.numofTree[rootb]+=num1
            self.numofTree.pop(roota)
            self.parent[roota]=rootb
    def groupNum(self):
        return len(self.numofTree)

points=[[0,0],[0,1],[1,2],[2,1],[1,1]]
position=[[0,0,0],[0,0,0],[0,0,0]]
u=unionfind(position)
for ite in points:
    u.insert(tuple(ite))
    print u.groupNum()
