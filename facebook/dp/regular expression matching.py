# -*- coding: utf-8 -*-
'''
0 0 = true, 最后要dp[len(s)][len(p)], if p[j-1]==* and j>=2: dp[i][j]=dp[i-1][j] and same(s[i-1],p[j-2]) and i>0
但记得都是从 i=0 开始

'''
# time complexity is O(mn)



def match(s,p):
    dp=[]
    for i in range(0,len(s)+1):
        dp.append([])
        for j in range(0,len(p)+1):
            dp[i].append(False)
    dp[0][0]=True
    for i in range(0,len(s)+1):
        for j in range(1,len(p)+1):
                # match * first
                if p[j-1]=='*' and j>=2:
                    dp[i][j]= i>0 and dp[i-1][j] and  same(s[i-1],p[j-2]) or dp[i][j-2]

                else:
                    dp[i][j]=i>0 and dp[i-1][j-1] and same(s[i-1],p[j-1])
    return dp[len(s)][len(p)]
def same(s,t):
    return s==t or t=='.'


s=['aa','aa','aaa','aa','aa','ab','aab']
p=['a','aa','aa','a*','.*','.*','c*a*b']
for i in range(0,7):
    print(match(s[i],p[i]))
