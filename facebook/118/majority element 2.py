# -*- coding: utf-8 -*-
'''
用 m,n cm, cn分别代表可能的majority elements 以及它出现的个数
如果遇到一个ite 等于m 或n， 那么cm+=1 或cn+=1,else如果cm==0，
那么把m换成ite，cm=1，n同理，如果以上都不符合，也就是两个都不是，
选出m,n之后，开始重新过一遍计算他们出现的次数，如果大于1/3，就添加
'''




def majorityElement(nums):
    res=[]
    m,n,cm,cn=0,0,0,0
    for ite in nums:
        if ite==m:
            cm+=1
        elif ite==n:
            cn+=1
        elif cm==0:
            m=ite
            cm=1
        elif cn==0:
            n=ite
            cn=1
        else:
            cm-=1
            cn-=1
    cm,cn=0,0
    for ite in nums:
        if ite ==m:
            cm+=1
        elif ite==n:
            cn+=1
    if cm > len(nums)/3:
        res.append(m)
    if cn > len(nums)/3:
        res.append(n)
    return res