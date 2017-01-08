# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        ite = head
        last = RandomListNode(0)
        if ite == None:
            return None
        while ite != None:
            ite1 = RandomListNode(ite.label)
            ite1.random = ite.random
            ite.random = ite1
            if ite == head:
                last = ite1
            else:
                last.next = ite1
                last = last.next
            ite = ite.next
        ite = head
        new_head = head.random
        while ite != None:
            ran = ite.random.random
            if ran != None:
                ite.random.random = ran.random
            ite.random = ran
            ite = ite.next
        return new_head
