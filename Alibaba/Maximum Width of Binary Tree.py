class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def widthOfBinaryTree(root):
    def dfs(node, depth = 0, pos = 0):
        if node:
            yield depth, pos
            yield from dfs(node.left, depth + 1, pos * 2)
            yield from dfs(node.right, depth + 1, pos * 2 + 1)

    left = {}
    right = {}
    ans = 0
    for depth, pos in dfs(root):
        left[depth] = min(left.get(depth, pos), pos)
        right[depth] = max(right.get(depth, pos), pos)
        ans = max(ans, right[depth] - left[depth] + 1)

    return ans

a=TreeNode(1)
c=TreeNode(3)
d=TreeNode(5)
e=TreeNode(3)
a.left=c
c.left=d
c.right=e
print(widthOfBinaryTree(a))
