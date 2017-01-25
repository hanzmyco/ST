import copy
def dfs(i, dic, output, k, current, n):
    if k > 1:
        current.append(i)
        dic[i] = 1
        for j in xrange(i + 1, n + 1):
            dfs(j, dic, output, k - 1, current, n)
        current.pop()
    elif k == 1:
        current.append(i)
        output.append(copy.deepcopy(current))
        current.pop()
def iteration(n,k):
    output=[]
    que=[]
    for i in xrange(1,n-k+2):
        que.append([i])
    while len(que) !=0 and len(que[0])<k:
        top=que.pop(0)
        for i in xrange(top[len(top)-1]+1,n+1):
            top.append(i)
            new_c=copy.deepcopy(top)
            if len(new_c)==k:
                output.append(new_c)
                que.append(new_c)
                top.pop()

    print output


def combine(n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        output = []
        dic={}
        current=[]
        for i in xrange(1, n + 1):
            dfs(i, dic, output, k,current,n)

        print output

combine(4,2)
iteration(4,2)