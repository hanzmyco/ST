def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    l = len(s)
    if l == 0:
        return 0
    if s[0] == '0':
        return 0
    if l == 1:
        return 1
    dic = {}

    dic[0] = 1
    if s[0] == '1':
        if s[1] == '0':
            dic[1] = 1
        else:
            dic[1] = 2
    elif s[0] == '2':
        if s[1] == '0':
            dic[1] = 1
        elif int(s[1]) <= 6:
            dic[1] = 2
        else:
            dic[1] = 1
    else:
        if s[1] == '0':
            return 0
        else:
            dic[1] = 1
    for i in xrange(2, l):
        if s[i - 1] == '1':
            if s[i] == '0':
                dic[i] = dic[i - 2]
            else:
                dic[i] = dic[i - 1] + dic[i - 2]
        elif s[i - 1] == '2':
            if s[i] == '0':
                dic[i] = dic[i - 2]
            elif int(s[i]) <= 6:
                dic[i] = dic[i - 1] + dic[i - 2]
            else:
                dic[i] = dic[i - 1]
        elif s[i - 1] == '0':
            if s[i] == '0':
                return 0
            else:
                dic[i] = dic[i - 1]
        else:
            if s[i] == '0':
                return 0
            else:
                dic[i] = dic[i - 1]
    return dic[l - 1]

def decodeways(s):
    if s==None or len(s)==0:
        print 0
    dp=[1,1]
    if s[0]=='0':
        dp[1]=0
    for i in xrange(2,len(s)+1):
        current=0
        if s[i-1]!='0':
            current=dp[1]
        if 10<=int(s[i-2:i]) <=26:
            current+=dp[0]
        dp[0]=dp[1]
        dp[1]=current
    print dp[1]

decodeways('0')