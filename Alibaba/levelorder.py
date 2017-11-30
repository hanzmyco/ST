import queue
from collections import deque
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def leveloRDER(root):
    if not root:
        return None
    que = deque()


    que.append(root)
    output = []
    target=root
    while True:
        inner_output = []
        next_level = deque()
        while len(que)!=0:
            head = que.popleft()
            inner_output.append(head.val)
            if head.left!=None:
                next_level.append(head.left)
            if head.right!=None:
                next_level.append(head.right)
        if inner_output != []:
            output.append(inner_output)
        if len(next_level)!=0:
            que = next_level
            target=que.popleft()
            que.appendleft(target)

        else:
            break
    print(target.val)
    return output

a=TreeNode(3)
b=TreeNode(9)
c=TreeNode(28)
d=TreeNode(15)
e=TreeNode(7)
a.left=b
a.right=c
c.left=d
c.right=e
output=leveloRDER(a)
print(output)
