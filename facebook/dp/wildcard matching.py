# -*- coding: utf-8 -*-
'''
0 0 = true, 最后要dp[len(s)][len(p)],
if p[j-1]==* and dp[i][j]= dp[i-1][j]  and i>0
但记得都是从 i=0 开始

'''

# wild card match time complexity is O(m*n) as


def match(s,p):
    dp=[]
    for i in range(0,len(s)+1):
        dp.append([])
        for j in range(0,len(p)+1):
            dp[i].append(0)
    dp[0][0]=1
    for i in range(0,len(s)+1):
        for j in range(1,len(p)+1):
            # match * first
            if p[j-1]=='*':
                    dp[i][j]=i>0 and dp[i-1][j] or dp[i][j-1]
            else:
                    if i>0:
                        dp[i][j]=dp[i-1][j-1] and same(s[i-1],p[j-1])
    return dp[len(s)][len(p)]
def same(s,t):
    return s==t or t=='?'

s=['aa','aa','aaa','aa','aa','ab','aab']
p=['a','aa','aa','*','a*','?*','c*a*b']
for i in range(0,7):
    print (match(s[i],p[i]))
