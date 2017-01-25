class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head=head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        res=self.head.val
        i=2
        cur=self.head.next
        while cur!=None:
            if random.randint(0, i - 1) == 0:
                res=cur.val
            i+=1
            cur=cur.next
        return res