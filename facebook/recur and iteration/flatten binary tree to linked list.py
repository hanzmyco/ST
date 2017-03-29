def dfs_recur(root):
    l_head,l_end,r_head,r_end=None,None,None,None
    if root.left!=None:
        (l_head,l_end)=dfs_recur(root.left)
    if root.right!=None:
        (r_head,r_end)=dfs_recur(root.right)
    root.left=None
    if r_head!=None and l_head!=None:
        root.right=l_head
        l_end.right=r_head
        return (root,r_end)
    elif r_head!=None:
        root.right=r_head
        return (root,r_end)
    elif l_head!=None:
        root.right=l_head
        return (root,l_end)
    else:
        return (root,root)

def dfs_iteration(root):
    stack=[[root,None,None]] # store root, last, root's real right
    last=None
    l=1
    while l!=0:
        top=root[l-1]
        if top[0].left!=None:
            stack.append([top[0].left,top[0],None])
            l+=1
            top.left=None
            if top[0].right!=None:
                top[2]=top[0].right
            top[0].right=top[0].left
        elif top[0].right!=None:
            l-=1
            stack.pop()
            stack.append([top[0].right,top[0],None])
            l+=1







def flatten(root):
    if root==None:
        return None
    (head,end)=dfs_recur(root)

