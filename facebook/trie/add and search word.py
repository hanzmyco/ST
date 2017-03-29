# -*- coding: utf-8 -*-
'''
Trienode data stryctyre:
用字典存《key,value>对，key是字母，value是子节点，用一个isLeaf标示来分别是否是
叶子节点

对于匹配 '*',直接跳过所有连续的*，用一个deque存重新开始匹配的地方，如果没找到，就从这个的儿子开始找
比如 插入words abckad, 现在search一个 re : abc*d, 那么匹配外abc之后，直接过掉*，从d开始，然后trie节点从k开始，递归的匹配，不行
的话就把k的儿子a放进去，还是不行就放d进去，发现可以了，就停止匹配
'''

from collections import deque
class TrieNode(object):
    def __init__(self):
        self.isLeaf = 0
        self.children = {}


class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        children = self.root.children
        for index, ite in enumerate(word):
            if ite in children:
                t = children[ite]
            else:
                t = TrieNode()
                children[ite] = t
            children = t.children
            if index == len(word) - 1:
                t.isLeaf = 1

    def search_from_node(self, word, node):
        children = node.children
        for index, ite in enumerate(word):
            if ite in children:
                t = children[ite]
                children = t.children
                if index == len(word) - 1 and t.isLeaf:
                    return 1
            elif ite == '.':
                if index == len(word) - 1 and len(children) != 0:
                    for ite in children:
                        if children[ite].isLeaf:
                            return 1
                    return 0
                for c in children:
                    if self.search_from_node(word[index + 1:], children[c]):
                        return 1
                return 0
            else:
                return 0

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        '*' repesent any letter or no letter, wild card
        :type word: str
        :rtype: bool
        """
        if self.search_from_node(word, self.root):
            return True
        return False



    def search_RE(self,word,root):
        ite=root
        for i in xrange(0,len(word)):
            if word[i] !='*' and word[i]!='.':
                if word[i] in ite.children:
                    ite=ite.children[word[i]]
                    if i ==len(word)-1 and ite.isLeaf:
                        return True
                else:
                    return False
            elif word[i] == '.':

                result=False
                for node_word in ite.children:
                    if ite.children[node_word].isLeaf and i == len(word)-1:
                        return True
                    result = result or self.search_RE(word[i+1:],ite.children[node_word])
                    if result:
                        return True
                return False


            else:
                j=i
                while j<len(word) and word[j]=='*':
                    j+=1
                if j==len(word):
                    return True
                que=deque()
                que.append(ite)
                res=False
                while len(que)!=0:
                    top_ite=que.popleft()
                    for node_char in top_ite.children:
                        if node_char ==word[j] or word[j]=='.':
                            if j==len(word)-1 and top_ite.children[node_char].isLeaf:
                                return True
                            elif j==len(word)-1 and top_ite.children[node_char].isLeaf==0:
                                return False
                            res=res or self.search_RE(word[j+1:],top_ite.children[node_char])
                            if res==True:
                                return True
                        que.append(top_ite.children[node_char])
                return res

wd=WordDictionary()
wd.addWord("abckad")
print wd.search_RE("abc*d",wd.root)
