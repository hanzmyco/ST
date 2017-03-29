# -*- coding: utf-8 -*-
'''
'''

'''
time complexity is k^n
dfs iteration的时候，每个node除了存current字符窜，还要存下一个长度的时候，map对应的每个字母是不是用了
'''
from collections import deque

def iterative(map,s):
    output=['']
    for ite in s:
        cur=[]
        for res in output:
            for letter in map[int(ite)]:
                cur.append(res+letter)
        output=cur
    print output
    print len(output)
def bfs_iteration(map,s):
    output=deque()
    output.append('')
    this_l=1
    for digit in s:
        last_l=this_l
        this_l=0
        for i in xrange(0,last_l):
            top = output.popleft()
            for letter in map[int(digit)]:
                output.append(top+letter)
                this_l+=1
    print output
    print len(output)

def dfs_recur(map,s,output,current):
    if len(s)==1:
        for letter in map[int(s)]:
            output.append(current+letter)
        return
    for letter in map[int(s[0])]:
        dfs_recur(map,s[1:],output,current+letter)
    return
def dfs_iteration(map,s):
    stack=[]
    output=[]
    current=''
    stack.append([current,len(map[int(s[0])])*[0]])
    while len(stack)!=0:
        top=stack[len(stack)-1]
        children=top[1]
        current=top[0]
        digit=len(current)
        tag=0
        if digit==len(s)-1:
            for index in xrange(0, len(children)):
                    output.append(current + map[int(s[digit])][index])
                    stack[len(stack) - 1][1][index] = 1
        else:
            for index in xrange(0,len(children)):
                if children[index]==0:
                    stack[len(stack) - 1][1][index] = 1
                    stack.append([current+map[int(s[digit])][index],len(map[int(s[digit+1])])*[0]])
                    tag=1
                    break
        if tag==0:
            stack.pop()
    print output
    print len(output)
def recur(map,s):
    output=[]
    if len(s)>1:
        res=recur(map,s[1:])
        for ite in map[int(s[0])]:
            for ite_str in res:
                output.append(ite+ite_str)
    else:
        for ite in map[int(s[0])]:
            output.append(ite)
    return output


s='279'
map={2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r','s'], 8: ['t', 'u','v'], 9: ['w', 'x','y','z']}
#iterative(map,s)
#print recur(map,'279')
bfs_iteration(map,s)
output=[]
dfs_recur(map,s,output,'')
print output
print len(output)
output=[]
s='279'
dfs_iteration(map,s)