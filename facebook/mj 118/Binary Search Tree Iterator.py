## 中序遍历用一个stack然后再用另一个指针找寻栈顶元素右孩子最小左孩子

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        current = root
        self.stack = []
        while current != None:
            self.stack.append(current)
            current = current.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) != 0

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        val = node.val
        node = node.right
        while node != None:
            self.stack.append(node)
            node = node.left
        return val

