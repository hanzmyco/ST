# -*- coding: utf-8 -*-
'''
快慢指针找到中间点，把后半部分REVERSE一下，然后直接和前半部分比
'''


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
        new_head = last.next
        last.next = new_head.next
        new_head.next = slow.next
        slow.next = new_head


    while slow.next != None:
        slow = slow.next
        if pre.val != slow.val:
            return False
        pre = pre.next
    return True