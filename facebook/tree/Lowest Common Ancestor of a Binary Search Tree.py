# -*- coding: utf-8 -*-
'''
利用bst的性质，第一个只有一个数会在两值中间，那就是答案了

'''

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root==None:
            return None
        minn=min(p.val,q.val)
        maxx=max(p.val,q.val)
        if minn<=root.val<=maxx:
            return root
        elif root.val >maxx:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return self.lowestCommonAncestor(root.right,p,q)