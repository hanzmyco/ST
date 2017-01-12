def recur(n):
    if n==1:
        return 1
    if n==0:
        return 0
    return recur(n-1)+recur(n-2)