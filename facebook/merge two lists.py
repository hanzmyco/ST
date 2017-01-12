def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 == None:
        return l2
    elif l2 == None:
        return l1
    dummy = ListNode(0)
    ite1 = l1
    ite2 = l2
    tail = dummy
    if l1.val <= l2.val:
        dummy.next = l1
        l1 = l1.next
    else:
        dummy.next = l2
        l2 = l2.next
    tail = tail.next
    while l1 != None and l2 != None:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1 != None:
        tail.next = l1
    else:
        tail.next = l2
    return dummy.next