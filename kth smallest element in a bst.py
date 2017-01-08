class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def helper(root,k,target):
    if root==None:
        return 0
    num_left=helper(root.left,k,target)
    if target!=None:
        return 0
    if num_left+1==k:
        target=root
        return 0
    num_right=helper(root.right,k-num_left-1,target)
    if target!=none:
        return 0
    return num_left+num_right+1

#target= None
#root= TreeNode(1)
#helper(root,1,target)
#print target.val

a=[1,2,3]
print a[1:2]
