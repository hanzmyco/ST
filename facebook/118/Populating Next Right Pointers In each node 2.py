# -*- coding: utf-8 -*-
'''
用leftmost决定下一层的最左边，cur等于leftmost，连接的时候注意用p，p往右边走，
cur如果连接了就往右边走，注意p没有孩子的话就一直往右走
'''

def connect(self, root):
    if root == None:
        return
    leftMost=root
    while leftMost:
        p=leftMost
        while p!=None and p.left==None and p.right==None:
            p=p.next
        if p==None:
            return
        if p.left!=None:
            leftMost=p.left
        else:
            leftMost=p.right
        cur=leftMost
        while p!=None:
            if cur==p.left:
                if p.right!=None:
                    cur.next=p.right
                    cur=cur.next
                p=p.next
            elif cur==p.right:
                p=p.next
            else:
                if p.left==None and p.right==None:
                    p=p.next
                    continue
                if p.left!=None:
                    cur.next=p.left
                else:
                    cur.next=p.right
                cur=cur.next
