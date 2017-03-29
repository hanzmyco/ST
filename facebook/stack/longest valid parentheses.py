# -*- coding: utf-8 -*-
'''
记录start，开始时start=0，start用来标记现在所有valid的（最早位置
开始遍历，如果s[i]=='（'就把i放到stack里，如果遇到'）'就看看现在stack的长度，如果空了，意味着前面的已经被记录了，并且现在不valid
那么就让start=i+1， 如果不空，就pop出来，如果pop完之后空了，证明现在合格valid，并且可以和前面的结合，那么更新res=max(res,i-start+!).
如果pop完之后还不空，那么证明前面的没匹配完，但是stack栈顶之后的都匹配完了，所以这时候用i-栈顶就行


'''


def longestValidParentheses(s):
    stack = []
    start = 0
    res = 0
    for i in xrange(0, len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                start = i + 1
            else:
                stack.pop()
                if len(stack) == 0:
                    res = max(res, i - start + 1)
                else:
                    res = max(res, i - stack[len(stack) - 1])
    return res