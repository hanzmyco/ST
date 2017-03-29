# -*- coding: utf-8 -*-
'''

两个方向的迭代法都是用中序遍历

double linked list to bst :
空间复杂度： stack的size是树的高度，为Log(n) （因为是bst所以一定是规则的），用快慢指针找中间的点来做中序遍历
时间复杂度： nlogn

BST TO dll:
迭代： stack的最大size为树的高度，log n ，额外空间是O(1), last只有在被pop出来的时候，也就是左边空了，才更新为当前
时间复杂度： 中序遍历的时间，O(n)


'''
class DoublyListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next =next
        self.pre = next
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def bst2dl_recur(root):
    lhead, lend,rhead,rend=None,None,None,None
    if root.left!=None:
        (lhead,lend)=bst2dl_recur(root.left)
        root.left=lend
        lend.right=root
    if root.right!=None:
        (rhead,rend)=bst2dl_recur(root.right)
        root.right=rhead
        rhead.left=root
    if lhead!=None and rhead!=None:
        return (lhead,rend)
    elif rhead!=None and lhead==None:
        return (root,rend)
    elif lhead!=None and rend==None:
        return (lhead,root)
    else:
        return (root,root)

def bst2dl_iter(root):
    stack=[root]
    l=1
    # use tag to identify the head
    tag=1
    head=None
    last=None
    while l!=0:
       top=stack[l-1]
       if top.left!=None:
           stack.append(top.left)
           l+=1
           top.left=None
           continue
       else:
           if tag:
               head=top
               tag=0
           if last!=None:
               top.left=last
               last.right=top
           last=top
           stack.pop()
           l -= 1
           if top.right!=None:
               stack.append(top.right)
               l+=1
    return head

# 中序遍历
def dl2bst_iter(head):
    end=head
    while end.next!=None:
        end=end.next
    fast=head
    slow=head
    while fast.next != end.next and fast.next.next != end.next:  # use this to check boundary
        slow = slow.next
        fast = fast.next.next
    root = TreeNode(slow.val)
    stack = [[root,head,slow,end]]
    l=1
    while l!=0:
        top=stack[l-1]
        if top[0].left==None and top[0].right==None:   #first time
            if top[1].next==top[2]: # one node
                top[0].left=TreeNode(top[1].val)
            elif top[1].next==slow.pre: # two node
                left=TreeNode(top[1].val)
                left.right=TreeNode(slow.pre.val)
                top[0].left=left
            else:
                fast=top[1]
                slow=fast
                while fast.next!=top[2] and fast.next.next!=top[2]:
                    slow=slow.next
                    fast=fast.next.next
                top[0].left=TreeNode(slow.val)
                stack.append([top[0].left,top[1],slow,top[2].pre])
                l+=1
        else:  # deal the right
            stack.pop()
            l-=1
            if top[2].next==top[3]: # one node
                top[0].right=TreeNode(top[3].val)
            elif top[2].next==top[3].pre:
                right=TreeNode(top[3].pre.val)
                right.right=TreeNode(top[3].val)
                top[0].right=right
            else:
                fast = top[2].next
                slow = fast
                while fast.next != top[3].next and fast.next.next != top[3].next:
                    slow = slow.next
                    fast = fast.next.next
                top[0].right = TreeNode(slow.val)
                stack.append([top[0].right,top[2].next, slow, top[3]])
                l+=1
    return root



def dl2bst_recur(head,end):
    if head ==end:
        return TreeNode(head.val)
    # 快慢指针的起始条件是3个元素，所以要定义一个元素和2个元素的情况
    elif head.next==end:
        root=TreeNode(head.val)
        root.right=TreeNode(end.val)
        return root
    slow=head
    fast=head
    while fast.next!=end.next and fast.next.next!=end.next :  # use this to check boundary
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
g=DoublyListNode(7)
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
f.next=g
g.pre=f
#root=doublelist2bst(a)
root=dl2bst_iter(a)
print a




'''
a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
d=TreeNode(4)
e=TreeNode(5)
f=TreeNode(6)
g=TreeNode(7)
a.right=b
c.left=a
c.right=e
e.left=d
e.right=f
#root=bst2dl_recur(c)[0]
root=bst2dl_iter(c)
print a
'''

