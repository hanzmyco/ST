def dfs(self, root):
    full_path = []
    left_path = []
    if root.left != None:
        left_path = self.dfs(root.left)
    right_path = []
    if root.right != None:
        right_path = self.dfs(root.right)

    if len(left_path) != 0:
        full_path.extend([str(root.val) + '->' + ite for ite in left_path])
    if len(right_path) != 0:
        full_path.extend([str(root.val) + '->' + ite for ite in right_path])
    if len(full_path) == 0:
        return [str(root.val)]
    return full_path


def binaryTreePaths(self, root):
    if root == None:
        return []
    return self.dfs(root)