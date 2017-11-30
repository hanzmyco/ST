def rob(root):
    res=robSub(root)
    return max(res[0],res[1])

def robSub(root):
    if root==None:
        return [0,0]
    left=robSub(root.left)
    right=robSub(root.right)
    res=[0,0]
    # res 0 ,root don't get rob
    res[0]=max(left[0],left[1])+max(right[0]+right[1])
    res[1]=root.val+left[0]+right[0]