class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """

        self.stack=[]
        for index in xrange(len(nestedList)-1,-1,-1):
            self.stack.append(nestedList[index])

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            return self.que.pop.getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """

        while len(self.stack)!=0:
            t=self.stack[len(self.stack)-1]
            if t.isInteger():
                return True
            self.stack.pop()
            for i in xrange(len(t.getList())-1,-1,-1):
                self.stack.append(t.getList()[i])
        return False
