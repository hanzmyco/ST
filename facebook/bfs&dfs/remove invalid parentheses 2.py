# -*- coding: utf-8 -*-
'''
非常玄妙，时间复杂度大概是o (n^2)
检测')'错误的时候，大概是k*m词，k是一共有多少个这种错误，m是每种错误有多少种解决方法，
m最多是 n/k种，所以正面总时间是n/k *k 是o(n)。反过来的时候，长度变为 n-k, 同理可证
时间为o(n-k),那么总时间是 n* (n-k)为 o(n^2)
'''
def dfs_p(s,ch,lasti,lastj,ans):
    cnt=0
    for i in xrange(lasti,len(s)):
        if s[i]=='(' or s[i]==')':
            if s[i]!=ch:
                cnt+=1
            else:
                cnt-=1
        if cnt>=0:
            continue
        for j in xrange(lastj,i+1):
            if s[j]==ch and (j==lastj or s[j-1]!=ch):
                dfs_p(s[:j]+s[j+1:],ch,i,j,ans)
        return
        # 到i的最右边的时候，会跳过上面return那一段

    if ch==')':
        return dfs_p(s[::-1],'(',0,0,ans)
    ans.append(s[::-1])










def dfs(s,ch,lasti,lastj,ans):
    cnt=0
    for i in xrange(lasti,len(s)):
        if s[i]=='(' or s[i]==')':
            if s[i]!=ch:
                cnt+=1
            else:
                cnt-=1
        if cnt >=0: # left is more or equal
            continue
        for j in xrange(lastj,i+1):
            if s[j]==ch and (j==lastj or s[j-1]!=ch):  #这一个递归的第一次或者前面一个有非）的插入
                dfs(s[:j]+s[j+1:],ch,i,j,ans)  #因为每次都缩短了一个，所以其实 last是本次开始的第一个，
        return
    if ch==')':
        return dfs(s[::-1],'(',0,0,ans)
    ans.append(s[::-1])

def dfs_begin(s):
    ans=[]
    dfs(s,')',0,0,ans)
    return ans

s=['()())()','(a)())()',')(','x(','(((k()((']

for test in s:
    print dfs_begin(test)

