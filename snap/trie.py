class TrieNode(object):
    def __init__(self, x):
        self.val = x
        self.isleaf = False
        self.children = {}

class Trie(object):
    root=None
    def __init__(self):
        self.root = TrieNode(0)
    def insert(self, word):
        children=self.root.children
        for i in xrange(0,len(word)):
            c = word[i]
            if c in children:
                t = children[c]
            else:
                t = TrieNode(c)
                children[c]=t
            children = t.children
            if i == len(word)-1:
                t.isleaf=True
    def nextNode(self, char, node):
        children=node.children
        if char in children:
            return children[char]
        else:
            return None

    def search(self,word):
        t = self.searchNode(word)

        if t != None and t.isleaf ==True:
            return True
        else:
            return False

    # return if there is any word in the trie starts with the given prefix
    def startsWith(self,prefix):
        if self.searhNode(prefix) == None:
            return False
        else:
            return True

    def searchNode(self, str1):
        children = self.root.children
        t = TrieNode(0)
        for i in xrange(0,len(str1)):
            c = str[i]
            if c in children:
                t = children[c]
                children = t.children
            else:
                return None
        return t



