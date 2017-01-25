def dfs(map,li,n,l): #11 22 33 44 55 66
    for i in li:
        if i not in map:
            map[i]=[1,l]
        dfs(map,li,n,l+1)

