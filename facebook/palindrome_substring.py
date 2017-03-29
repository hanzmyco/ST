# -*- coding: utf-8 -*-
'''
问sub string里有几个palidrome
'''

def palindrome_substring(s):
    dp={}
    pali_sub={}
    for i in xrange(0,len(s)):
        dp[(i,i)]=1
        pali_sub[s[i]]=1

    for i in xrange(0,len(s)-1):
        if s[i]==s[i+1]:
            dp[(i,i+1)]=1
            if s[i:i+2] not in pali_sub:
                pali_sub[s[i:i+2]]=1
        else:
            dp[(i,i+1)]=0

    for l in xrange(2,len(s)):
        for i in xrange(0,len(s)-l):
            if dp[(i+1,i+l-1)] and s[i]==s[i+l]:
                    dp[(i,i+l)]=1
                    if s[i:i+l+1] not in pali_sub:
                        pali_sub[s[i:i+l+1]]=1
            else:
                    dp[(i, i + l)] = 0
    print pali_sub
    return len(pali_sub)


s='ababa'
s1='baabceffe'
print palindrome_substring(s1)

