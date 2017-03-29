# -*- coding: utf-8 -*-
'''
不用标isleaf是因为默认每个单词长度一样，所有叶节点都是一个词的终结
判重有问题
'''

class TrieNode(object):
    def __init__(self):
        self.isLeaf=False
        self.children=[None]*26
        self.word_list=[]
class Trie(object):
    def __init__(self,words):
        self.root=TrieNode()
        for w in words:
            cur=self.root
            for index,ch in enumerate(w):
                idx=ord(ch)-ord('a')
                if cur.children[idx] ==None:
                    cur.children[idx]=TrieNode()
                cur=cur.children[idx]
                if index==len(w)-1:
                    cur.isLeaf=True
                    cur.word_list.append(w)
class DFS(object):
    def __init__(self,trie,list_ch):
        self.trie=trie
        self.list_ch=list_ch
        self.len=len(self.list_ch)
        self.output=[]
        self.dic=[0]*self.len
    def dfs(self,cur,index):
        #保证cur.children是存在的
        if cur.children[ord(self.list_ch[index])-ord('a')]==None or self.dic[index]==1:
            return
        cur=cur.children[ord(self.list_ch[index])-ord('a')]
        self.dic[index]=1
        if cur.isLeaf:
            self.output.extend(cur.word_list)
        for i in xrange(0,self.len):
            if i >0 and i-1 != index and self.list_ch[i] == self.list_ch[i - 1]:
                    continue

            self.dfs(cur,i)
        self.dic[index]=0
    def find_word(self):
        for i in xrange(0,len(self.list_ch)):
            if i>0:
                if self.list_ch[i]==self.list_ch[i-1]:
                    continue
            self.dfs(self.trie.root,i)
        print self.output


array=['a','b','c','a']
dic=['a','aa','ba','cba','abca','bca']
trie=Trie(dic)
array.sort()
solution=DFS(trie,array)
solution.find_word()