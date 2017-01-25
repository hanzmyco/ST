def findCelebrity(n):
    res=0
    for i in xrange(0,n):
        if knows(res,i):
            res=i
    for i in xrange(0,n):
        if i!=res and knows(res,i) or knows(i,res)==False :
            return -1

    return res