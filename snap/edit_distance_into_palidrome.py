def edit_distance_to_Palidrome(s):
    t=s[::-1]
    l=len(s)
    dMatrix=[]
    for i in xrange(0,l+1):
        dMatrix.append([])
    dMatrix[0].append(0)
    for i in xrange(1,l+1):
        dMatrix[0].append(i)
        dMatrix[i].append(i)
    for i in xrange(1,l+1):
        for j in xrange(1,l+1):
            if s[i-1]==t[j-1]:
                dMatrix[i].append(dMatrix[i-1][j-1])
            else:
                dMatrix[i].append(min(dMatrix[i-1][j-1],dMatrix[i-1][j],dMatrix[i][j-1])+1)
    return dMatrix[l][l]/2


s=['tanbirahmed','shahriarmanzoor','monirulhasan','syedmonowarhossain','sadrulhabibchowdhury','mohammadsajjadhossain']

for si in s:
    print edit_distance_to_Palidrome(si)