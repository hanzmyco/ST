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

def widthOfBinaryTree2(root):
    def dfs(node, left_dic,right_dic,depth = 0, pos = 0):
        if node:
            if depth not in left_dic:
                left_dic[depth]=pos
                right_dic[depth]=pos
            if pos <left_dic[depth]:
                left_dic[depth]=pos
            elif pos > right_dic[depth]:
                right_dic[depth]=pos

            dfs(node.left, left_dic,right_dic,depth + 1, pos * 2)
            dfs(node.right,left_dic,right_dic,depth + 1, pos * 2 + 1)

    left = {}
    right = {}
    ans = 0
    dfs(root,left,right,0,0)
    for depth in left:
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
print(widthOfBinaryTree2(a))