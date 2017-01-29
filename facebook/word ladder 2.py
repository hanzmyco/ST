from collections import deque
import copy
def add_output(map,ite,endWord,output):
    out=[[ite,endWord]]
    res = []
    tag=False
    while True:
        if tag:
            break
        for li in out:
                children=li[0]
                fathers=map[children]
                if fathers==None:
                    tag=True
                    continue
                for pa in fathers:
                    temp=copy.deepcopy(li)
                    temp.insert(0,pa)
                    res.append(temp)
        out=copy.deepcopy(res)
        res=[]

    output.extend(out)
def ladderLength(beginWord, endWord, wordList):
    map={beginWord:None}
    que=deque()
    que.append(beginWord)
    output=[]
    tag=False
    sub_que=deque()
    while len(que)!=0:

        ite=que.popleft()
        if ite =='rex':
            print 'lol'
        for j in xrange(0,len(ite)):
            for i in xrange(0,26):
                letter=str(unichr(97+i))
                if letter==ite[j]:
                    continue
                sub_word=ite[:j]+letter+ite[j+1:]
                if sub_word ==beginWord:
                    continue
                if  sub_word in wordList :
                    if sub_word == endWord:
                        add_output(map,ite,endWord,output)
                        tag=True

                        #if ite[:j]+letter+ite[j+1:] not in map:
                        #    map[ite[:j] + letter + ite[j + 1:]]=[ite]
                        #else:
                         #   map[ite[:j] + letter + ite[j + 1:]].append(ite)
                    else:
                        if sub_word not in map:
                            map[sub_word]=[ite]
                        else:
                            map[sub_word].append(ite)
                        sub_que.append(sub_word)
        if len(que)==0:
            if tag:
                return output
            que=copy.deepcopy(sub_que)
            sub_que=deque()

    return output

#print ladderLength('hit','cog',set(["hot","dot","dog","lot","log","cog"]))
#print ladderLength('a','c',set(['a','b','c']))
print ladderLength('red','tax',set(["ted","tex","red","tax","tad","den","rex","pee"]))
