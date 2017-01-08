class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def isSymmetric(root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        l1=[root]
        l2=[]
        while len(l1)!=0:
            ite=l1.pop(0)
            if ite!=None:
                if ite.left!=None or ite.right!=None:
                    l2.append(ite.left)
                    l2.append(ite.right)
                    if len(l1)==0:
                        print l2
                        head=0
                        tail=len(l2)-1
                        while head<tail:
                            if (l2[head]==None and l2[tail]!=None) or (l2[head]!=None and l2[tail]==None):
                                return False
                            elif l2[head]!=None and l2[tail]!=None and l2[head].val!=l2[tail].val:
                                return False
                            head+=1
                            tail-=1
                        l1=l2
                        l2=[]
        return True
a=TreeNode(2)
b=TreeNode(3)
c=TreeNode(3)
d=TreeNode(4)
e=TreeNode(5)
e1=TreeNode(5)
f=TreeNode(4)
g=TreeNode(8)
h=TreeNode(9)
i=TreeNode(9)
j=TreeNode(8)
a.left=b
a.right=c
b.left=d
b.right=e
c.left=e1
c.right=f
e.left=g
e.right=h
f.left=i
f.right=j
print isSymmetric(a)
