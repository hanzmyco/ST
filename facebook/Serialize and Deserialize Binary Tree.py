class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def serialize(root):
    que = collections.deque()
    que.append(root)
    result=''
    while len(que) != 0:
        ite = que.popleft()
        if ite != None:
            result += str(ite.val)+' '
            que.append(ite.left)
            que.append(ite.right)
        else:
            result += '# '
    return result
def deserialize(data):
    if len(data)==0:
        return None
    list_node=data.strip().split(' ')
    index=0
    root=TreeNode(int(list_node[index]))
    que = collections.deque()
    que.append(root)index+=1
    while len(que)!=0:
        t=que.popleft()
        if index==len(list_node):
            break
        if list_node[index]!='#':
            cur=TreeNode(int(list_node[index]))
            que.append(cur)
            t.left=cur
        index+=1
        if index==len(list_node):
            break
        if list_node[index]!='#':
            cur=TreeNode(int(list_node[index]))
            que.append(cur)
            t.right=cur
        index+=1
    return root

a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
d=TreeNode(4)
e=TreeNode(5)
a.left=b
a.right=c
c.left=d
c.right=e
str1=serialize(a)
print str1
root=deserialize(str1)
print 'lol'
