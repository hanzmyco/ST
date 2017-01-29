from collections import deque
def ladderLength(beginWord, endWord, wordList):
    map={beginWord:1}
    que=deque()
    que.append(beginWord)
    while len(que)!=0:
        ite=que.popleft()
        for j in xrange(0,len(ite)):
            for i in xrange(0,26):
                letter=str(unichr(97+i))
                if ite[:j]+letter+ite[j+1:] in wordList and ite[:j] + letter + ite[j + 1:] not in map:
                    if ite[:j] + letter + ite[j + 1:] == endWord:
                        return map[ite] + 1

                    map[ite[:j]+letter+ite[j+1:]]=map[ite]+1
                    que.append(ite[:j]+letter+ite[j+1:])

    return 0

print ladderLength('a','c',set(['a','b','c']))
