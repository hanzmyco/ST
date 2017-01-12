import heapq
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


def merge_k_sorted_list(lists):
    head=ListNode(0)
    new_li=[]
    for i in lists:
        if i !=None:
            new_li.append((i.val,i))

    heapq.heapify(new_li)
    if len(new_li)==0:
        return None
    head.next=heapq.heappop(new_li)[1]
    if head.next.next!=None:
        heapq.heappush(new_li,(head.next.next.val,head.next.next))
    tail=head.next
    print head.next.val
    while len(new_li)!=0:
        ite=heapq.heappop(new_li)[1]
        print ite.val
        if ite.next!=None:
            heapq.heappush(new_li,(ite.next.val,ite.next))
        tail.next=ite
        tail=ite
    return head.next


a=ListNode(1)
b=ListNode(2)
c=ListNode(2)
d=ListNode(1)
e=ListNode(1)
f=ListNode(2)
a.next=b
b.next=c
d.next=e
e.next=f
li=[a,d]
print merge_k_sorted_list(li)
print 'lol'