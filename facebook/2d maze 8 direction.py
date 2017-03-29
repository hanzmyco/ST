# -*- coding: utf-8 -*-
'''
follow up 2:
每次que里存的是新的一层，然后pop出来top，开始遍历下一层，如果top访问了下一层某个点，
那么就把下一层点x 的father标为top，那么top的邻接点就不用访问x了。对于top的第二个点y，
看看在que里的有没有能吸收y的，如果有，那么就break，留给另外的点来处理y，如果没有，
就在相交子节点对里面加入x,y。相当于top的所有可达下层节点都有可能冲突，如果无法分配给
其他同层节点

'''

from collections import deque
def isRoad(x,y):
    return 0.3
def isRoad0(x,y):
    return True
def print_path(node):
    return
def find_path_larger_than_a(a,s,t):
    que=deque()
    que.append((s[0],s[1]))
    map[(s[0],s[1])]=(1,None)  #store the probability and parent
    while len(que)!=0:
        top=que.popleft()
        prob=map(top)[0]
        # 找到了
        if (top[0]-1,top[1])==(t[0],t[1]):
            print_path((t[0]-1,t[1]))
            return

        if (top[0]-1,top[1]) not in map:
            if prob*isRoad(top[0]-1,top[1])>=a:
                map[(top[0]-1,top[1])]=(prob*isRoad(top[0]-1,top[1]),top)
                que.append((top[0]-1,top[1]))

        elif prob*isRoad(top[0]-1,top[1]) > map[(top[0]-1,top[1])]:
            map[(top[0] - 1, top[1])]=(prob * isRoad(top[0] - 1, top[1]),top)
            que.append((top[0]-1,top[1]))

        
        # 其他七个方向




        '''
        do it for 8 directions
        '''
def find_L_Route(s,t):
    que = deque()
    que.append(s)
    father={}
    father[s] = (None)
    sub_que = deque()
    res=[]
    collide=set()
    while len(que)!=0:
        top=que.popleft()
        if top ==t:
            res.append(print_path(top))
            continue
        x,y=top[0]-1,top[1]
        # first children 不用担心allocate
        top_tag=1
        collide_sub=[(x,y)]
        if (x,y) not in father:
            if top_tag:
                father[(x,y)]=top
                top_tag=0
            else:
                # 判断能否被allocate给其他节点
                allocate=1
                for ite in que:
                    if accesible(ite,(x,y)): # can allocate to others
                        allocate=0
                        break
                if allocate:
                    collide_sub.append((x,y))




