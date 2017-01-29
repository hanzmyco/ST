# use trie to help the dfs, use the value of a trie node to store the current prefix,


class trie_node(object):
    def __init__(self,val):
        self.val=val
        self.children={}
        self.isLeaf=False
class trie(object):
    def __init__(self):
        self.root=trie_node('')
    def insert(self,word):
        ite=self.root
        for index,i in enumerate(word):
            if i in ite.children:
                ite=ite.children[i]
            else:
                prefix=ite.val
                ite.children[i]=trie_node(prefix+i)
                ite=ite.children[i]
            if index == len(word)-1:
                ite.isLeaf=True
    def dfs(self,board,m,n,i,j,dic,root,output):
        if board[i][j] in root.children:
            ite=root.children[board[i][j]]
            dic[(i,j)]=1
            if ite.isLeaf:
                if ite.val=='aaa':
                    print 'found'
                if ite.val not in output:

                    output.add(ite.val)
            if i >= 1 and ((i - 1, j) not in dic or dic[(i - 1, j)] == 0):
                self.dfs(board, m, n, i - 1, j, dic,ite, output)
            if j >= 1 and ((i, j - 1) not in dic or dic[(i, j - 1)] == 0):
                self.dfs(board, m, n, i, j - 1, dic,ite,output)
            if i < m - 1 and ((i + 1, j) not in dic or dic[(i + 1, j)] == 0):
                self.dfs(board, m, n, i + 1, j, dic,ite,output)
            if j < n - 1 and ((i, j + 1) not in dic or dic[(i, j + 1)] == 0):
                self.dfs(board, m, n, i, j + 1, dic,ite,output)
            del dic[(i,j)]

    def search(self, board, m, n):
        dic = {}
        output = set()
        for i in xrange(0, m):
            for j in xrange(0, n):
                self.dfs(board, m, n, i, j, dic, self.root, output)
        return list(output)

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

        return trie1.search(board, m, n)

board=["ab","aa"]
words=["aba","baa","bab","aaab","aaa","aaaa","aaba"]
#words=['aa','aaa','aaaa']
print findWords(board,words)
