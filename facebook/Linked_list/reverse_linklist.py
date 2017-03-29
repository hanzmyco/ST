class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def recursion(head):
    if head == None:
        return None
    if head.next != None:
        new_head= recursion(head.next)
        head.next.next=head
        head.next=None
        return new_head
    else:
        return head

def iterative(head):
        if head == None or head.next == None:
            return head
        new_head = head
        ite = head.next
        new_head.next = None
        while ite != None:
            real_ite = ite.next
            ite.next = new_head
            new_head = ite
            ite = real_ite
        return new_head
