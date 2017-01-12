import heapq

# at most k transactions
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices)==0:
        return 0
    n=len(prices)
    g=[]
    l=[]
    for i in xrange(0,n):
        g.append([])
        l.append([])
        for j in xrange(0,3):
            g[i].append(0)
            l[i].append(0)
    for i in xrange(1,len(prices)):
        diff=prices[i]-prices[i-1]
        for j in xrange(1,3):
            l[i][j]=max(g[i-1][j-1]+max(diff,0),l[i-1][j]+diff)
            g[i][j]=max(g[i-1][j],l[i][j])
    return g[n-1][2]


print maxProfit([1,2])