class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def buildTree(inorder,postorder):
    if len(postorder)==0:
        return None
    root=TreeNode(postorder[-1])
    left_end=0
    right_begin=0
    for i in range(0,len(inorder)):
        if inorder[i]==root.val:
            left_end=i-1
            right_begin=i+1
            break
    left=buildTree(inorder[:left_end+1],postorder[:left_end+1])
    right=buildTree(inorder[right_begin:len(inorder)],postorder[len(postorder)-right_begin:len(postorder)])


