def dfs(root):
    l_head,l_end,r_head,r_end=None,None,None,None
    if root.left!=None:
        (l_head,l_end)=dfs(root.left)
    if root.right!=None:
        (r_head,r_end)=dfs(root.right)
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
def flatten(root):
    if root==None:
        return None
    (head,end)=dfs(root)