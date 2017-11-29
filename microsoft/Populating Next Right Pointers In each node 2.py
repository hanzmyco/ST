# -*- coding: utf-8 -*-

'''
head是下一层的头，在遍历上一层的时候准备下一个
pre记录上一个点（下一个层的），cur是该层当前点，每次都是用该层来连接下一层
'''

def connect(root):
    head = None # head of next level
    pre = None # the leading node on the next level
    cur = root # current node of current level

    while cur !=None:
        while cur!=None:
            # left child
            if cur.left!=None:
                if pre!=None:  # the next level has been initialized
                    pre.next=cur.left
                else: #  we must set the head , 为了下一层的遍历做准备
                    head=cur.left
                pre=cur.left

            # right child
            if cur.right!=None:
                if pre!=None:
                    pre.next=cur.right
                else:
                    head=cur.right
                pre=cur.right

            cur=cur.next
        cur=head  # prepare for next level
        pre=None
        head=None
