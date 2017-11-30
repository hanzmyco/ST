def postorderTraversal(root):
    stack1=[]
    stack2=[]
    stack1.append(root)
    while stack1:
        top=stack1.pop()
        if top.left!=None:
            stack1.append(top.left)
        if top.right!=None:
            stack1.append(top.right)
        stack2.append(top)
    stack2.reverse()
    return stack2