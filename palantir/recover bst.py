# -*- coding: utf-8 -*-
'''
这题应该没问题了
'''

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def inorder(root, pre, first, second):
    if root == None:
        return
    inorder(root.left, pre, first, second)
    if pre == None:
        pre = root
    else:
        if pre.val > root.val:
            if first == None:
                first = pre
            second = root
        pre = root
    inorder(root.right, pre, first, second)


def recoverTree(root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    pre = None
    first = None
    second = None
    inorder(root, pre, first, second)
    if first != None and second != None:
        temp = first.val
        first.val = second.val
        second.val = temp

a=TreeNode(0)
b=TreeNode(1)
a.left=b
recoverTree(a)
print 'lol'