# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def recur(root, res):
        sub_left, sub_right = None, None
        if root.left != None:
            sub_left = recur(root.left, res)
        if root.right != None:
            sub_right = recur(root.right, res)
        part_res = root.val
        left = root.val
        right = root.val
        if sub_left != None and sub_left>0:
            part_res += sub_left
            left += sub_left
        if sub_right != None and sub_right>0:
            part_res += sub_right
            right += sub_right
        res[0] = max(res[0], part_res)
        return max(left, right)

def maxPathSum(root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        res = [0]
        final = recur(root, res)
        return max(final, res[0])
a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
a.left=b
a.right=c
print maxPathSum(a)