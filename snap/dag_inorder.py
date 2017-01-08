class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left=None
        self.right=None

def inorder_traverse(root,dic,k):
    left_num=0
    right_num=0
    dic[root] = 1
    if root.left!=None and root.left not in dic:
        k_th_char=inorder_traverse(root.left,dic,k)
        if k_th_char !=None: # found
            return k_th_char

    if root.left in dic:
        left_num = dic[root.left]

    if left_num==k-1 :
        return root.val


    if root.right!=None and root.right not in dic:
        k_th_char =inorder_traverse(root.right,dic,k-left_num-1)
        if k_th_char!=None:
            return k_th_char
    if root.right in dic:
        right_num=dic[root.right]
    dic[root]=left_num+right_num+1
    return




a=TreeNode('a')
b=TreeNode('b')
c=TreeNode('c')
d=TreeNode('d')
e=TreeNode('e')
f=TreeNode('f')
a.left=b
a.right=c
b.left=d
b.right=e
c.right=e
e.left=f

dic={}
print inorder_traverse(a,dic,1)
dic={}
print inorder_traverse(a,dic,2)
dic={}
print inorder_traverse(a,dic,3)
dic={}
print inorder_traverse(a,dic,4)
dic={}
print inorder_traverse(a,dic,5)