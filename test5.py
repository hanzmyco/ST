# Complete the function below.
def height(word,dic):
    if len(dic[word])==0: # no offsprings
        return 1
    child_height=0
    for ite in dic[word]:
        child_height=max(child_height,height(ite,dic))
    return child_height+1

def one_distance(w1,w2): # w1 is longer than w2
    if len(w1)-len(w2)!=1:
        return False
    for index in xrange(0,len(w1)):
        if w1[:index]+w1[index+1:] == w2:
            return True
    return False
def succesor(w1):
    out=[]
    for index in xrange(0,len(w1)):
        out.append(w1[:index]+w1[index+1:])
    return out
def longestChain(words):
    length = len(words)
    offspring = {}
    fathers = {}
    words.sort(lambda x, y: cmp(len(x), len(y)), reverse=True)
    for ite in xrange(0, length):
        fathers[words[ite]]=1
    for i in xrange(0, length):
        offspring[words[i]] = []
        children=succesor(words[i])
        for ite in children:
            if ite in fathers:
                offspring[words[i]].append(ite)
                fathers[ite]=fathers[word[i]]
    output = 0
    for ite in fathers:
        if fathers[ite] == 1 and len(ite) > output:
            output = max(height(ite, offspring), output)
    return output