# -*- coding: utf-8 -*-
'''
不用标isleaf是因为默认每个单词长度一样，所有叶节点都是一个词的终结
'''

import copy
class TrieNode(object):
    def __init__(self):
        self.startWith=[]
        self.children=[None]*26
class Trie(object):
    def __init__(self,words):
        self.root=TrieNode()
        for w in words:
            cur=self.root
            for ch in w:
                idx=ord(ch)-ord('a')
                if cur.children[idx] ==None:
                    cur.children[idx]=TrieNode()
                #这里存前缀树，每一个结点存所有以这个为前缀的词
                cur.children[idx].startWith.append(w)
                cur=cur.children[idx]
    def findByprefix(self,prefix):
        ans=[]
        cur=self.root
        for ch in prefix:
            idx=ord(ch)-ord('a')
            if cur.children[idx]==None:
                return ans
            cur=cur.children[idx]
        ans.extend(cur.startWith)
        return ans
def wordSquares(words):
    ans=[]
    if words==None or len(words)==0:
        return ans
    leng=len(words[0])
    trie=Trie(words)
    cur=[]
    for w in words:
        cur.append(w)
        search(leng,trie,ans,cur)
        cur.pop()
    return ans
def search(l,trie,ans,cur):
    if len(cur)==l:
        ans.append(copy.deepcopy(cur))
        return
    # 这里要看一下几何结构，prefix是cur的最大行
    idx=len(cur)
    prefix=''
    for s in cur:
        prefix+=s[idx]
    startWith=trie.findByprefix(prefix)
    for sw in startWith:
        cur.append(sw)
        search(l,trie,ans,cur)
        cur.pop()
words=["area","lead","wall","lady","ball"]
print wordSquares(words)



