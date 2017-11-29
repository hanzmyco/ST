class TreeNode(object):
    def __init__(self, val=None):
        self.val=val
        self.left=None
        self.right=None


def postOrder(root):
    if not root:
        return
    stack=[]
    stack.append(root)
    pre=None
    l_stack=1
    while l_stack!=0:
        current=stack[l_stack-1]
        if not pre or pre.left==current or pre.right==current: # top down
            if current.left:
                stack.append(current.left)
                l_stack+=1
            elif current.right:
                stack.append(current.right)
                l_stack+=1
        elif pre==current.left:  # left is finished
            if current.right:
                stack.append(current.right)
                l_stack+=1
        else:  # right is finished or there is no children
            print current.val
            stack.pop()
            l_stack-=1
        pre=current

def inOrder(root):
    if not root:
        return
    stack=[]
    l=0
    pointer=root
    while pointer!=None or l!=0:
        if pointer !=None:
            stack.append(pointer)
            pointer=pointer.left
            l+=1
        else:
            pointer=stack[l-1]
            stack.pop()
            l-=1
            print pointer.val
            pointer=pointer.right





a=TreeNode(0)
b=TreeNode(1)
c=TreeNode(2)
d=TreeNode(3)
a.left=b
a.right=c
c.right=d
#postOrder(a)
inOrder(a)