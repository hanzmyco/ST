def one_distance(w1,w2): # w1 is longer than w2
    if len(w1)-len(w2)!=1:
        return False
    for index in xrange(0,len(w1)):
        if w1[:index]+w1[index+1:] == w2:
            return True
    return False

def height(index,dic):
    if len(dic[index])==0: # no offsprings
        return 1
    child_height=0
    for ite in dic[index]:
        child_height=max(child_height,height(ite,dic))
    return child_height+1

def longestChain(words):
    length = len(words)
    offspring = {}
    fathers = []
    words.sort(lambda x, y: cmp(len(x), len(y)), reverse=True)
    for ite in xrange(0, length):
        fathers.append(1)
    for i in xrange(0, length):
        offspring[i] = []
        j = i + 1
        while j < length and len(words[j]) == len(words[i]):
            j += 1

        while j < length and len(words[j]) == len(words[i]) - 1:
            if one_distance(words[i], words[j]):
                offspring[i].append(j)
                fathers[j] = 0
            j += 1
    output = 0
    for ite in xrange(0,length):
        if fathers[ite] == 1 and len(words[ite]) > output:
            output = max(height(ite, offspring), output)
    return output


