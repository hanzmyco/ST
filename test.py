def cmp1(s1,s2):
    return len(s1) > len(s2)
a=['a','bcd','cd']


a.sort(lambda x,y: cmp(len(x),len(y)), reverse=True)
print a


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


def longestChain(words):
    length = len(words)
    offspring = {}
    fathers = []
    for ite in xrange(0, length):
        fathers.append(1)
    for i in xrange(0, length):
        offspring[i] = []
        for j in xrange(0, length):
            if j != i and len(words[j]) < len(words[i]):
                if one_distance(words[i], words[j]):
                    offspring[i].append(j)
                    fathers[j] = 0
    output = 0
    print fathers
    print offspring
    for ite in xrange(0, length):
        if fathers[ite] == 1 and len(words[ite]) > output:
            h = height(ite, offspring)
            print h
            output = max(h, output)
    return output
