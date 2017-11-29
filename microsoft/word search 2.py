# -*- coding: utf-8 -*-
'''
trie只在叶节点存整个单词，用这个来消除重复

'''

class trie_node(object):
    def __init__(self,val=None):
        self.val=val
        self.children=[None]*26
class trie(object):
    def __init__(self):
        self.root=trie_node()
    def insert(self,word):
        ite=self.root
        for index,letter in enumerate(word):
            if ite.children[ord(letter) - ord('a')] ==None:
                ite.children[letter]=trie_node()
            ite=ite.children[letter]
            if index == len(word)-1:
                ite.val=word
        
def dfs(self,board,i,j,root,output):
        if board[i][j] in root.children:
            ite=root.children[board[i][j]]
            c=board[i][j]
            board[i][j]='#'
            if ite.val!=None:
                output.append(ite.val)
                ite.val=None
            if i >= 1 and board[i-1][j]!='#':
                self.dfs(board, i - 1, j,ite, output)
            if j >= 1 and board[i][j-1]!='#':
                self.dfs(board,i, j - 1,ite,output)
            if i < len(board) - 1 and board[i+1][j]!='#':
                self.dfs(board, i + 1, j,ite,output)
            if j < len(board[0]) - 1 and board[i][j+1]!='#':
                self.dfs(board, i, j + 1, ite,output)
            
            board[i][j]=c
        
def findWords(board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        m = len(board)
        n = 0
        if m > 0 and len(words) > 0:
            n = len(board[0])
        else:
            return False
        trie1 = trie()
        for word in words:
            trie1.insert(word)
        output = []
        for i in xrange(0, m):
            for j in xrange(0, n):
                self.dfs(board, i, j, dic, self.root, output)
        return output
board=["ab","aa"]
words=["aba","baa","bab","aaab","aaa","aaaa","aaba"]
#words=['aa','aaa','aaaa']
print findWords(board,words)
