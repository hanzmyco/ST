# -*- coding: utf-8 -*-
''' use dp, instead of putting boolean for each state, store the previous index and the
word generated from last index to current as tuple
用dp，和第一题不同，不存boolean数组，存可以和现在这个长度组成新单词的之前的长度，
迭代写法怎么做 ？？
'''
def wordBreak(s,wordDict):
    map = {}
    for ite in wordDict:
        if len(ite) not in map:
            map[len(ite)] = set()
        map[len(ite)].add(ite)
    dp = [['']]
    for i in xrange(1, len(s) + 1):
        dp.append([])
    for i in xrange(0, len(s) + 1):
        for j in xrange(0, i):
            if len(dp[j])!=0 and i - j in map and s[j:i] in map[i - j]:
                for ite in dp[j]:
                    if j !=0:
                        dp[i].append(ite+' '+s[j:i])
                    else:
                        dp[i].append(s[j:i])
    return dp[len(s)]

def wordBreak1(s,wordDict):
    map = {}
    for ite in wordDict:
        if len(ite) not in map:
            map[len(ite)] = set()
        map[len(ite)].add(ite)
    dp = [[(0)]]
    for i in xrange(1, len(s) + 1):
        dp.append([])
    for i in xrange(0, len(s) + 1):
        for j in xrange(0, i):
            if len(dp[j]) != 0 and i - j in map and s[j:i] in map[i - j]:
                    dp[i].append(j)
    #return dfs(dp,len(s))
    return non_recur(dp,len(s),s)
def dfs(dp,l):
    if l==0:
        return ['']
    output=[]
    for ite in dp[l]:
        for prefix in dfs(dp,ite):
            if prefix !='':
                output.append(prefix+' '+s[ite:l])
            else:
                output.append(s[ite:l])
    return output


def non_recur(dp,l,s):
    stack=[l]
    dic={}
    while len(stack)!=0:
        top=stack[len(stack)-1]
        if top not in dic:
            dic[top]=[]
        if top==0:
            dic[top]=['']
            stack.pop()
            continue
        tag=0
        for children in dp[top]:
            if children not in dic:
                stack.append(children)
                tag=1
                break
        if tag:
            continue
        for children in dp[top]:
            for prefix in dic[children]:
                if prefix!='':
                    dic[top].append(prefix+' '+s[children:top])
                else:
                    dic[top].append(s[children:top])
        stack.pop()
    return dic[l]









s='catsanddog'
dict = ["cat", "cats", "and", "sand", "dog"]
print wordBreak1(s,dict)
