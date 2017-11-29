# -*- coding: utf-8 -*-
'''
dfs的时间复杂度是 n!, factorial(n)
'''
import collections






def get_one_example(s):
    a = 0
    b = 0
    # b is the mistake when ) is more
    # a is the mistake when ( is more
    left_bad_index=[]
    right_bad_index=[]
    stack=[]
    l_stack=0
    temp=[]
    for index in range(0,len(s)):
        temp.append(s[index])
        if s[index]=='(':
            stack.append(index)
            l_stack+=1
        elif s[index]==')':
            if l_stack==0: # mistake
                right_bad_index.append(index)
            else:
                stack.pop()
                l_stack-=1

    num=0
    if l_stack!=0:
        for index in stack:
            temp.pop(index-num)
            num+=1
    if right_bad_index !=[]:
        for index in right_bad_index:
            temp.pop(index - num)
            num += 1
    output=''
    for ite in temp:
        output+=ite
    print (output)

def calc_Mistake(s):
    a=0
    b=0
    # b is the mistake when ) is more
    # a is the mistake when ( is more
    for c in s:
        a+={'(':1,')':-1}.get(c,0)
        b+=a<0
        a=max(a,0)
    return a+b

def dfs_helper(s,visited):
    numMistake=calc_Mistake(s)
    if numMistake ==0:
        return [s]
    ans=[]
    for index in range(0,len(s)):
        if s[index] in ('(',')'):
            new_s=s[:index]+s[index+1:]
            if new_s not in visited:
                visited.add(new_s)
                if calc_Mistake(new_s) <=numMistake: # reduce mistake
                    ans.extend(dfs_helper(new_s,visited))
    return ans

def dfs_helper1(s,visited,numMistake):
    ans=[]
    for index in range(0,len(s)):
        if s[index] in ('(',')'):
            new_s=s[:index]+s[index+1:]
            if new_s not in visited:
                visited.add(new_s)
                new_mistakes=calc_Mistake(new_s)
                if new_mistakes==0:
                    ans.append(new_s)
                else:
                    if new_mistakes <= numMistake:
                        ans.extend(dfs_helper1(new_s,visited,new_mistakes))
    return ans

def dfs(s):
    num_mistake=calc_Mistake(s)
    if num_mistake==0:
        return [s]
    visited=set([s])
    return dfs_helper1(s,visited,num_mistake)


def bfs(s):
    mi = calc_Mistake(s)
    if mi == 0:
        return [s]
    ans=[]
    visited=set([s])
    queue=collections.deque([s])
    while queue:
        t = queue.popleft()
        for x in range(len(t)):
            if t[x] not in ('(', ')'):
                continue
            ns = t[:x] + t[x + 1:]
            if ns not in visited:
                num_mistake=calc_Mistake(ns)
                if num_mistake <= mi:
                    if num_mistake!=0:
                        queue.append(ns)
                    else:
                        ans.append(ns)
                    mi=num_mistake

                visited.add(ns)
    return ans

def bfs2(s):
        if len(s) == 0:
            return ['']
        begin_mistake = calc_Mistake(s)
        if begin_mistake == 0:
            return [s]
        output = []
        que = collections.deque()
        que.append(s)
        visited = {}
        l = 1
        last_mistake = begin_mistake
        while l != 0:
            top = que.popleft()
            l -= 1
            for index in range(0, len(top)):
                next_str = top[:index] + top[index + 1:]
                if next_str in visited:
                    continue
                visited[next_str] = 1
                num_mis_new = calc_Mistake(next_str)
                if num_mis_new == 0:
                    output.append(next_str)
                    last_mistake = 0
                elif num_mis_new <= last_mistake:
                    que.append(next_str)
                    last_mistake = num_mis_new
                    l += 1
        return output


s=['()())()','(a)())()',')(','x(']
s1=['x(']
s2=['))(()(','n']
s3='))'

get_one_example(s[3])





'''
for i in s:
    print dfs(i)
    print bfs(i)
'''