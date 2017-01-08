def findfirstbad(n):
    start=1
    end=n
    while start+1<end:
        mid=(start+end)/2
        if badversion(mid):
            end=mid
        else:
            start=mid
    if badversion(start):
        return start
    return end

def isvadversion(i)
    return True