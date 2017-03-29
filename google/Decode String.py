def decodeString(s):
    stack=[]
    i=0
    res=''
    while i < len(s):
        conse_num=0
        while -1<=ord(s[i+conse_num])-ord('1')<=8:
            conse_num+=1

        if conse_num!=0:
            stack.append(int(s[i:i+conse_num]))
            i+=conse_num
            continue
        # not number
        elif s[i] ==']':
            out=''
            while stack[len(stack)-1]!='[':
                out=stack[len(stack)-1]+out
                stack.pop()
            duplicate_out=''
            stack.pop()
            repete_time=stack.pop()
            for j in xrange(0,repete_time):
                duplicate_out+=out
            if len(stack)!=0:
                stack.append(duplicate_out)
            else:
                res+=duplicate_out
        else:
            stack.append(s[i])
        i+=1
    if len(stack)!=0:
        for ite in stack:
            res+=ite
    return res

s=['3[a]2[bc]','3[a2[c]]','2[abc]3[cd]ef']
for i in s:
    print decodeString(i)