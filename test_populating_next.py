def populating_next(root):
    p=root
    leftmost=None

    # find left most in next level
    while p!=None:
        if p.left==None and p.right==None:
            p=p.next
        elif p.left!=None:
            leftmost=p.left
            break
        elif p.right!=None:
            leftmost=p.right
            break
    if leftmost==None:
        return

    # as long as we have leftmost in next level
    while leftmost!=None:
        ite=leftmost
        while p!=None:
            if p.left==ite:
                if p.right!=None:
                    ite.next=p.right
                    ite=ite.next
            p=p.next
            #find next node on last level with children
            while p!=None and p.left==None and  p.right==None:
                p=p.next

            if p!=None:
                if p.left!=None:
                    ite.next=p.left
                elif p.right!=None:
                    ite.next=p.right

                ite=ite.next

        p=leftmost
        while p != None:
            if p.left == None and p.right == None:
                p = p.next
            elif p.left != None:
                leftmost = p.left
                break
            elif p.right != None:
                leftmost = p.right
                break
        if p==None:
            break
