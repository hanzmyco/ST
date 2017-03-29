# -*- coding: utf-8 -*-
'''
中序遍历用一个stack存，初始化的时候就找到最下层的左孩子，next函数就把栈顶元素pop出来，然后把node指向pop出来的右孩子，之后
不断的又把左孩子入栈
'''
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

