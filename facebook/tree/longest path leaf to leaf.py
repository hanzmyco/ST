# -*- coding: utf-8 -*-
'''
递归，每次求的是左子树的高度以及左子树里节点之间的最大距离，右边也是
然后再对现在的max_h,max_d进行计算

'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        
def maxLeafDistance(root):
    l_d,l_h, r_d,r_h=0,0,0,0
    if root.left!=None:
        l_d,l_h=maxLeafDistance(root.left)
    if root.right!=None:
        r_d,r_h=maxLeafDistance(root.right)
    max_h=max(l_h,r_h)+1
    max_d=max(l_h+r_h+1,l_d,r_d)
    return max_d,max_h

a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
d=TreeNode(4)
e=TreeNode(5)
f=TreeNode(6)
g=TreeNode(0)
h=TreeNode(0)
a.left=b
a.right=c
b.left=d
b.right=e
d.right=f
e.left=g
g.right=h
print maxLeafDistance(a)