import Queue
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
a=Queue.Queue()
a.put(5)
print(a.get())

def leveloRDER(root):
    if not root:
        return []
    que = Queue.Queue()
    que.put(root)
    output = []
    while True:
        inner_output = []
        next_level = Queue.Queue()
        while not que.empty():
            head = que.get()
            inner_output.append(head.val)
            if head.left!=None:
                next_level.put(head.left)
            if head.right!=None:
                next_level.put(head.right)
        if inner_output != []:
            output.append(inner_output)
        if not next_level.empty():
            que = next_level
        else:
            break
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
