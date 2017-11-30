import queue
import copy
def build_link(word,wordSet,link_dic):
    for index in range(0,len(word)):
        letter=ord('a')
        while letter <=ord('z'):
            if chr(letter)!=word[index]:
                candidate=word[:index]+chr(letter)+word[index+1:]
                if  candidate in wordSet:
                    if word not in link_dic:
                        link_dic[word]=set([candidate])
                    else:
                        link_dic[word].add(candidate)
            letter+=1
def dfsprint(child,father_dic,output_list,begin_word):
    for ite in output_list:
        ite.append(child)
    return_list=[]
    if child!=begin_word:
        for father in father_dic[child]:
                new_output=copy.deepcopy(output_list)
                one_list=dfsprint(father,father_dic,new_output,begin_word)
                return_list.extend(one_list)
    else:
        return_list.extend(output_list)
    return return_list
def findLadders(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: List[List[str]]
    """
    large_wordlist=wordList
    large_wordlist.append(beginWord)
    large_wordlist.append(endWord)
    wordSet=set(large_wordlist)
    link_dic={}
    for word in wordList:
        build_link(word,wordSet,link_dic)
    showed_set=set()
    que=queue.Queue()
    que.put(beginWord)
    showed_set.add(beginWord)
    father_dic={}
    output_all=[]
    next_que = set()
    tag=True
    father_dic[beginWord]=set()


    while not que.empty():
        top=que.get()
        if top in link_dic:
            if top =='ted':
                print('found')
            for child in link_dic[top]:
                if child not in showed_set :
                    if child not in father_dic :
                        father_dic[child] = set()
                    father_dic[child].add(top)
                    if child !=endWord:
                        next_que.add(child)
                    else:
                        tag=False
        if que.empty() and tag:
            que=queue.Queue()
            for ite in next_que:
                que.put(ite)
                showed_set.add(ite)
            next_que=set()

    output = [[]]
    new_output = dfsprint(endWord, father_dic, output,beginWord)
    output_all.extend(new_output)

    return output_all
print(findLadders('hit','cog',["hot","dot","dog","lot","log",'cog']))
#print(findLadders('a','c',['a','b','c']))
print(findLadders("red","tax",["ted","tex","red","tax","tad","den","rex","pee"]))
