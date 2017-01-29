class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def iteration(arr):
    stack=[]
    l=0
    for ite in arr:
        node=TreeNode(ite)
        if l!=0:
            if stack[l-1].val < ite:
                stack[l-1].right=node
            else:
                left=stack.pop()
                l-=1
                while l!=0 and stack[l-1].val > ite:
                    left=stack.pop()
                    l-=1
                if l!=0:
                    stack[l-1].right=node
                node.left=left


        stack.append(node)
        l+=1
    while l !=1:
        stack.pop()
        l-=1
    return stack[0]

input=[2,4,3,5,1]
root=iteration(input)
print root



def dfs(arr,begin,end):
    (val,index)=min(arr[begin:end+1])
    left,right=None,None
    root = TreeNode(val)
    if index>begin:
        left=dfs(arr,begin,index-1)


    if index<end:
        right=dfs(arr,index+1,end)

    root.left=left
    root.right=right
    return root

arr=[2,4,1,3,5,6]
arr=[1,2,3,4,5]
arr=[5,4,3,2,1]
arr1=[]
for index, ite in enumerate(arr):
    arr1.append((ite,index))

root=dfs(arr1,0,len(arr1)-1)
print root
