def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head == None or head.next == None:
        return True
    slow = head
    fast = head
    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next
    last = slow.next
    pre = head
    while last.next != None:
        tmp = last.next
        last.next = tmp.next
        tmp.next = slow.next
        slow.next = tmp
    while slow.next != None:
        slow = slow.next
        if pre.val != slow.val:
            return False
        pre = pre.next
    return True