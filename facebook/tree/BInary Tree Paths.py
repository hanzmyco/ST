# -*- coding: utf-8 -*-
'''
递归左右两子树，分别返回了list Of paths，再把这些paths的每个元素+上root的val组成一个新的list
'''

def dfs(self, root):
    full_path = []
    left_path = []
    if root.left != None:
        left_path = self.dfs(root.left)
    right_path = []
    if root.right != None:
        right_path = self.dfs(root.right)

    if len(left_path) != 0:
        full_path.extend([str(root.val) + '->' + ite for ite in left_path])
    if len(right_path) != 0:
        full_path.extend([str(root.val) + '->' + ite for ite in right_path])
    if len(full_path) == 0:
        return [str(root.val)]
    return full_path


def binaryTreePaths(self, root):
    if root == None:
        return []
    return self.dfs(root)