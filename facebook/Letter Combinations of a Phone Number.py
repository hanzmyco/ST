def iterative(map,s):
    total=1
    output=['']
    for ite in s:
        cur=[]
        for res in output:
            for letter in map[int(ite)]:
                cur.append(res+letter)
        output=cur
    print output
    print len(output)


def recur(map,s):
    output=[]
    if len(s)>1:
        res=recur(map,s[1:])
        for ite in map[int(s[0])]:
            for ite_str in res:
                output.append(ite+ite_str)
    else:
        for ite in map[int(s[0])]:
            output.append(ite)
    return output


s='279'
map={2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r','s'], 8: ['t', 'u','v'], 9: ['w', 'x','y','z']}
iterative(map,s)
print recur(map,'279')