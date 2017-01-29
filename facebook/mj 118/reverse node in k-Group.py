# -*- coding: utf-8 -*-
'''

'''

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

# 左闭右开
def reverse(head,tail):
    pre=tail
    while head!=tail:
        t=head.next
        head.next=pre
        pre=head
        head=t
    return pre
def reverseKGroup(head,k):
    cur=head
    for i in xrange(0,k):
        if cur==None:
            return head
        cur=cur.next
    new_head=reverse(head,cur)
    head.next=reverseKGroup(cur,k)
    return new_head

a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
d=ListNode(4)
e=ListNode(5)
a.next=b
b.next=c
c.next=d
d.next=e
k=2
head=reverseKGroup(a,k)
print head