import collections
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def flatten_linkedlist(head,head_set):
    if head ==None:
        return (None,None)
    ite=head
    tail=ListNode(0)
    while ite !=None:
        if ite not in head_set:
            head_set[ite]=1
            if type(ite.val) == ListNode:
                if ite.val not in head_set:
                    head_set[ite.val]=0
                ite.val=None

        tail=ite
        ite=ite.next
    for ite in head_set:
        if head_set[ite]==0:
            head_set[ite] = 1
            (new_head, new_tail)=flatten_linkedlist(ite,head_set)
            tail.next=new_head
            tail=new_tail

    return (head,tail)

a=ListNode(1)
#c=ListNode(3)
e=ListNode(5)
#d=ListNode(e)
b=ListNode(e)
f=ListNode(6)
g=ListNode(b)
a.next=b
#c.next=d
e.next=f
f.next=g
head_set = collections.OrderedDict()
(new_head, new_tail)=flatten_linkedlist(a,head_set)
print new_head