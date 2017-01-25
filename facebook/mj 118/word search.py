def dfs(self, board, m, n, i, j, word, dic):
    if board[i][j] == word[0]:
        dic[(i, j)] = 1
        tag = False
        if len(word) == 1:
            return True
        if i >= 1 and ((i - 1, j) not in dic or dic[(i - 1, j)] == 0):
            tag = tag or self.dfs(board, m, n, i - 1, j, word[1:], dic)
        if j >= 1 and ((i, j - 1) not in dic or dic[(i, j - 1)] == 0):
            tag = tag or self.dfs(board, m, n, i, j - 1, word[1:], dic)
        if i < m - 1 and ((i + 1, j) not in dic or dic[(i + 1, j)] == 0):
            tag = tag or self.dfs(board, m, n, i + 1, j, word[1:], dic)
        if j < n - 1 and ((i, j + 1) not in dic or dic[(i, j + 1)] == 0):
            tag = tag or self.dfs(board, m, n, i, j + 1, word[1:], dic)
        dic[(i, j)] = 0
        return tag
    else:
        return False


def exist(self, board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    dic = {}
    m = len(board)
    n = 0
    if m > 0 and len(word) > 0:
        n = len(board[0])
    else:
        return False
    for i in xrange(0, m):
        for j in xrange(0, n):
            if self.dfs(board, m, n, i, j, word, dic):
                return True
    return False