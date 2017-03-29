class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
def dfs(root):
    left_wo,left_w,right_wo,right_w=0,0,0,0
    if root.left!=None:
        left_wo,left_w=dfs(root.left)
    if root.right!=None:
        right_wo,right_w=dfs(root.right)
    wo_root=max(left_wo,right_wo,left_w,right_w)
    w_root=1
    if root.left!=None and root.left.val==root.val+1:
        w_root=left_w+1
    if root.right!=None and root.right.val==root.val+1:
        w_root=max(w_root,right_w+1)
    return wo_root,w_root

def longestConsecutive(root):
    if root !=None:
        return max(dfs(root))
    return 0
a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
d=TreeNode(4)
e=TreeNode(5)
a.right=c
c.left=b
c.right=d
d.right=e
print longestConsecutive(a)

from collections import deque
def longestConsecutive(self, root):
    if not root:
        return 0
    ans, dq = 0, deque([[root, 1]])
    while dq:
        node, length = dq.popleft()
        ans = max(ans, length)
        for child in [node.left, node.right]:
            if child:
                l = length + 1 if child.val == node.val + 1 else 1
                dq.append([child, l])
    return ans
def longestConsecutive(self, root):
    if not root:
        return 0
    ans, stack = 0, [[root, 1]]
    while stack:
        node, length = stack.pop()
        ans = max(ans, length)
        for child in [node.left, node.right]:
            if child:
                l = length + 1 if child.val == node.val + 1 else 1
                stack.append([child, l])
    return ans


