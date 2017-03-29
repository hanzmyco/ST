# -*- coding: utf-8 -*-
'''
use dfs as intuitive, as each word cannot be used more than once in one path, use a hashmap to store whether one word has been used or not
和num of island不同的是，dfs时候除了第一层的开始点，其他每个点都有可能重复访问，
time complexity: m*n*3^k*4, k is the length of the word，

space complexity: k + k , k is the size of recursion ( height of the tree), as we delete dic[(i,j)], we only keep at most k statuses
 we can even do it on the board to make the space complexity to k
'''

def dfs_nonrecur(board,m,n,word):
    stack=[]
    dic={}
    visited={}
    for i in xrange(0,m):
        for j in xrange(0,n):
            if board[i][j]==word[0]:
                stack.append((i,j,0))
                dic[(i,j)]=1
                visited[(i,j)]=4
            while len(stack)!=0:
                top=stack[len(stack)-1]
                if visited[(top[0],top[1])]==4:
                    if  top[2] == len(word)-1:
                        return True
                if visited[(top[0],top[1])]== 4 and top[0] >= 1 and ((top[0]-1,top[1]) not in dic or dic[(top[0]-1,top[1])]==0) and word[top[2]+1]==board[top[0]-1][top[1]]:
                        stack.append((top[0]-1,top[1],top[2]+1))
                        dic[(top[0]-1,top[1])]=1
                        visited[(top[0]-1,top[1])]=4
                        visited[(top[0], top[1])]=3
                        continue
                elif visited[(top[0],top[1])]== 4:
                    visited[(top[0],top[1])]=3
                if visited[(top[0],top[1])]==3 and top[1] >= 1 and ((top[0],top[1]-1) not in dic or dic[(top[0],top[1]-1)]==0) and word[top[2]+1] == board[top[0]][top[1]-1]:
                        stack.append((top[0], top[1]-1, top[2] + 1))
                        dic[(top[0], top[1]-1)] = 1
                        visited[(top[0],top[1]-1)]=4
                        visited[(top[0], top[1])] = 2
                        continue
                elif visited[(top[0],top[1])]==3:
                        visited[(top[0], top[1])] = 2
                if visited[(top[0],top[1])]==2 and top[0] < m-1 and ((top[0] + 1, top[1]) not in dic or dic[(top[0]+1,top[1])]==0) and word[top[2]+1] == board[top[0] + 1][top[1]]:
                        stack.append((top[0] + 1, top[1], top[2] + 1))
                        dic[(top[0] + 1, top[1])] = 1
                        visited[(top[0]+1,top[1])]=4
                        visited[(top[0], top[1])] = 1
                        continue
                elif visited[(top[0],top[1])]==2:
                    visited[(top[0], top[1])] = 1


                if visited[(top[0],top[1])]==1 and top[1] < n-1 and ((top[0], top[1]+1) not in dic or dic[(top[0],top[1]+1)]==0) and word[top[2]+1] == board[top[0]][top[1]+1]:
                        stack.append((top[0], top[1]+1, top[2] + 1))
                        dic[(top[0], top[1]+1)] = 1
                        visited[(top[0],top[1]+1)]=4
                        visited[(top[0], top[1])] = 0
                        continue
                elif visited[(top[0],top[1])]==1:
                    visited[(top[0], top[1])] = 0
                if visited[(top[0],top[1])]==0:
                    dic[(top[0],top[1])]=0
                    stack.pop()

    return False


def dfs( board, m, n, i, j, word, dic):
    if board[i][j] == word[0]:
        dic[(i, j)] = 1
        tag = False
        if len(word) == 1:
            return True
        if i >= 1 and ((i - 1, j) not in dic or dic[(i - 1, j)] == 0):
            tag = tag or dfs(board, m, n, i - 1, j, word[1:], dic)
        if j >= 1 and ((i, j - 1) not in dic or dic[(i, j - 1)] == 0):
            tag = tag or dfs(board, m, n, i, j - 1, word[1:], dic)
        if i < m - 1 and ((i + 1, j) not in dic or dic[(i + 1, j)] == 0):
            tag = tag or dfs(board, m, n, i + 1, j, word[1:], dic)
        if j < n - 1 and ((i, j + 1) not in dic or dic[(i, j + 1)] == 0):
            tag = tag or dfs(board, m, n, i, j + 1, word[1:], dic)
        del dic[(i,j)]
        return tag
    else:
        return False


def exist( board, word):
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

    return dfs_nonrecur(board,m,n,word)
    '''
    for i in xrange(0, m):
        for j in xrange(0, n):
            if self.dfs(board, m, n, i, j, word, dic):
                return True
    return False
    '''
board=["ABCE","SFES","ADEE"]
word='ABCESEEEFS'
print exist(board,word)