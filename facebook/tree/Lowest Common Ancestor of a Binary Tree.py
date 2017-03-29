# -*- coding: utf-8 -*-
'''

也是左右两边找，关键是分别找到其中一个和另外一个，然后网上就行了
'''


def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if root == None:
        return None
    if root == p or root == q:
        return root
    left_res = None
    if root.left != None:
        left_res = self.lowestCommonAncestor(root.left, p, q)
    right_res = None
    if root.right != None:
        right_res = self.lowestCommonAncestor(root.right, p, q)
    if left_res != None and right_res != None:
        return root
    elif left_res != None:
        return left_res
    elif right_res != None:
        return right_res