# -*- coding: utf-8 -*-
'''
start end，start扎下来，end不停往后探，用表记录下来一路访问过的是要的字母的位置，之后start往后探的时候就用这个
'''

import collections

def redo(s,t):
    res=''
    minn=10000
    l1=len(s)
    l2=len(t)
    if l1==0 or l2==0:
        return ''
    if l2 == 1:
        if t in s:
            return t
        else:
            return ''
    start,end=0,-1
    position=collections.OrderedDict()
    num_t=l2
    num_each={}
    for ite in t:
        if ite not in num_each:
            num_each[ite]=1
        else:
            num_each[ite]+=1
    while start < l1 and end <l1:
        while start <l1 and s[start] not in num_each:
            start+=1
        if end==-1:
            end=start
        else:
            end+=1
        while end<l1 and num_t>0:
            if s[end] in num_each :
                if num_each[s[end]]>0:
                    num_t-=1
                num_each[s[end]]-=1
                position[end]=s[end]
                if num_t==0:
                   break
            end+=1
        if end==l1:
            break
        for index in position:
            if num_t==0:
                if end-index+1 <minn:
                    minn=end-index+1
                    res=s[index:end+1]
                if num_each[s[index]]==0:
                    num_t += 1
                num_each[s[index]]+=1
                del position[index]
            else:
                start=index
                break
    return res






def min_window_1(s,t):
    if len(s) == 0 or len(t) == 0:
        return None
    start = 0
    end = -1
    dic = {}
    len1 = len(s)
    len2 = len(t)
    if len2 == 1:
        if t in s:
            return t
        else:
            return ''

    for i in xrange(0, len(t)):
        if t[i] not in dic:
            dic[t[i]] = 1
        else:
            dic[t[i]] += 1
    num = 0
    minn = 100000
    output=''

    while start < len and end < len1:
        while start < len1 and s[start] not in dic:
            start += 1
        if start == len1:
            break
        if end ==-1:
            dic[s[start]] -= 1
            if dic[s[start]] >= 0:
                num += 1
            end = start+1 # the first time
        else:
            end+=1
        if end == len1:
            break

        while end < len1 and num < len2:
            if s[end] in dic:
                dic[s[end]] -= 1
                if dic[s[end]] >= 0:
                    num += 1
            end += 1
        end-=1  #go back to the last char in dic
        if end == len1:
            break


        while start < end and num==len2:
            if end-start+1<minn:
                minn=end-start+1
                output=s[start:end+1]
            start += 1
            dic[s[start-1]]+=1
            if dic[s[start-1]]>0:
                num-=1
                break
            else:
                while s[start] not in dic:
                    start+=1
    return output


def min_window_2(s,t):
    if len(s) == 0 or len(t) == 0:
        return None
    start = 0
    end = -1
    dic = {}
    len1 = len(s)
    len2 = len(t)
    if len2 == 1:
        if t in s:
            return t
        else:
            return ''

    for i in xrange(0, len(t)):
        if t[i] not in dic:
            dic[t[i]] = 1
        else:
            dic[t[i]] += 1
    num = 0
    minn = 100000
    output=''
    position=collections.OrderedDict()
    while start < len and end < len1:
        while start < len1 and s[start] not in dic:
            start += 1
        if start == len1:
            break
        if end ==-1:
            dic[s[start]] -= 1
            if dic[s[start]] >= 0:
                num += 1
            end = start+1 # the first time
            position[start]=s[start]

        else:
            end+=1
        if end == len1:
            break

        while end < len1 and num < len2:
            if s[end] in dic:
                dic[s[end]] -= 1
                if dic[s[end]] >= 0:
                    num += 1
                position[end]=s[end]
            end += 1
        end-=1  #go back to the last char in dic
        if end == len1:
            break

        for ite in position:
            start = ite

            if num!=len2:
                    break
            else:
                    if end - start + 1 < minn:
                        minn = end - start + 1
                        output = s[start:end + 1]
                    dic[position[ite]]+=1
                    if dic[position[ite]]>0:
                        num-=1
                    position.pop(ite)


    return output



s='adobecodebanc'
t='abc'
s1='aa'
t1='aa'
#print (min_window_2(s,t))
print (redo(s,t))