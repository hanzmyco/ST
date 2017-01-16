def maximalSquare(matrix):
    if len(matrix)==0 or len(matrix[0])==0:
        return 0
    m=len(matrix)
    n=len(matrix[0])
    res=0
    summ=[]
    for i in xrange(0,m):
        summ.append([])
        for j in xrange(0,n):
            summ[i].append(0)

    for i in xrange(0,m):
        for j in xrange(0,n):
            if matrix[i][j]=='1':
                t=1
            else:
                t=0
            if i >0:
                t+=summ[i-1][j]
            if j>0:
                t+=summ[i][j-1]
            if i >0 and j>0:
                t-=summ[i-1][j-1]
            summ[i][j]=t
            cnt=1
            k=min(i,j)
            while k>=0:
                d=summ[i][j]
                if i-cnt >=0:
                    d-=summ[i-cnt][j]
                if j-cnt >=0:
                    d-=summ[i][j-cnt]
                if i-cnt >=0 and j-cnt>=0:
                    d+=summ[i-cnt][j-cnt]
                if d ==cnt*cnt:
                    res=max(res,d)
                cnt+=1
                k-=1
    return res

print maximalSquare([['1','0'],['1','0']])