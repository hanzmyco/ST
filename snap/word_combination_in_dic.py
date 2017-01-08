from trie import *


def word_combine(array, dic):
    tree = Trie()
    for ite in dic:
        tree.insert(ite)
    print 'a'
    return helper(array, tree)


def dfs(array, tree, node,i, hash_t, current, output):
    if  i < len(array) and hash_t[i]==0:
        next_node=tree.nextNode(array[i],node)
        if next_node !=None:
            if next_node.isleaf:
                output.add(current+next_node.val)
            hash_t[i]=1
            for j in xrange(0,len(array)):
                dfs(array,tree,next_node,j,hash_t,current+next_node.val,output)
            hash_t[i]=0
        else:
            return
    else:
        return

def helper(array, tree):
    dic={}
    for index in xrange(0,len(array)):
        dic[index]=0
    output=set()
    for i in xrange(0,len(array)):
        dfs(array, tree,tree.root,i,dic,'',output)
    return output

array=['a','b','c','a']
dic=['a','aa','ba','cba','aabc','bbb']

print word_combine(array, dic)



