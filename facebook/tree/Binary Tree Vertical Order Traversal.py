# -*- coding: utf-8 -*-
'''
层次遍历，用que，记录最小最大值就好
'''



import collections

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def level_order(root):
    map = {0: [root.val]}
    que = collections.deque()
    que.append((root, 0))
    minn = 0
    while len(que) != 0:
        top = que.popleft()
        if top[0].left != None:
            if top[1] - 1 not in map:
                map[top[1] - 1] = [top[0].left.val]
            else:
                map[top[1] - 1].append(top[0].left.val)
            minn = min(minn, top[1] - 1)
            que.append((top[0].left, top[1] - 1))
        if top[0].right != None:
            if top[1] + 1 not in map:
                map[top[1] + 1] = [top[0].right.val]
            else:
                map[top[1] + 1].append(top[0].right.val)
            que.append((top[0].right, top[1] + 1))
    output = []
    for index in xrange(minn, minn + len(map)):
        output.append(map[index])
    return output

def verticalOrder(root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        return level_order(root)

a=TreeNode(3)
b=TreeNode(9)
c=TreeNode(20)
d=TreeNode(15)
e=TreeNode(7)
a.left=b
a.right=c
c.left=d
c.right=e
print verticalOrder(a)