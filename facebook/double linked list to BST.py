class DoublyListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = next
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def dl2bst_recur(head,end):
    if head ==end:
        return TreeNode(head.val)
    elif head.next==end:
        root=TreeNode(head.val)
        root.right=TreeNode(end.val)
        return root
    slow=head
    fast=head
    while fast.next!=None and fast.next.next!=None and slow.next!=end:  # use this to check boundary
        slow=slow.next
        fast=fast.next.next
    root=TreeNode(slow.val)
    root.left=dl2bst_recur(head,slow.pre)
    root.right=dl2bst_recur(slow.next,end)
    return root


def doublelist2bst(head):
    ite =head
    if ite==None:
        return None
    while ite.next!=None:
        ite=ite.next
    return dl2bst_recur(head,ite)

a=DoublyListNode(1)
b=DoublyListNode(2)
c=DoublyListNode(3)
d=DoublyListNode(4)
e=DoublyListNode(5)
f=DoublyListNode(6)
#g=DoublyListNode(7)
a.next=b
b.pre=a
b.next=c
c.pre=b
c.next=d
d.pre=c
d.next=e
e.pre=d
e.next=f
f.pre=e
#f.next=g
#g.pre=f
root=doublelist2bst(a)
print a

