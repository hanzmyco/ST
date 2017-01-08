class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def post_order(root,dic1):
    left=''
    if root.left!=None:
        left=post_order(root.left,dic1)

    right=''
    if root.right!=None:
        right=post_order(root.right,dic1)
    str1=left+right+root.val
    if str1 not in dic1:
        dic1[str1]=1
    else:
        dic1[str1]+=1
    return str1

root=TreeNode('10')
l1=TreeNode('8')
root.left=l1
l2=TreeNode('4')
l3=TreeNode('5')
l4=TreeNode('3')
l5=TreeNode('3')
l6=TreeNode('8')
l7=TreeNode('5')
l8=TreeNode('4')
l9=TreeNode('5')
l10=TreeNode('3')
l11=TreeNode('3')
l1.left=l2
l1.right=l3
l3.left=l4
root.right=l5
l5.left=l6
l5.right=l7
l6.left=l8
l6.right=l9
l7.left=l10
l9.left=l11

dic={}
dic1={}
post_order(root,dic1)
print dic1