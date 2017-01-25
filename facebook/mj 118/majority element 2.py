def majorityElement(nums):
    res=[]
    m,n,cm,cn=0,0,0,0
    for ite in nums:
        if ite==m:
            cm+=1
        elif ite==n:
            cn+=1
        elif cm==0:
            m=ite
            cm=1
        elif cn==0:
            n=ite
            cn=1
        else:
            cm-=1
            cn-=1
    cm,cn=0,0
    for ite in nums:
        if ite ==m:
            cm+=1
        elif ite==n:
            cn+=1
    if cm > len(nums)/3:
        res.append(m)
    if cn > len(nums)/3:
        res.append(n)
    return res