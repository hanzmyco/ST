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
