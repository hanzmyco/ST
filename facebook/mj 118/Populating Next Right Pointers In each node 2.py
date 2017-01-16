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
