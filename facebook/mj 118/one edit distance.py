def isOneEditDistance(s,t):
    for i in xrange(0,min(len(s),len(t))):
        if s[i]!=t[i]:
            if len(s) == len(t):
                return s[i+1:] == t[i+1:]
            elif len(s)<len(t):
                return s[i:] == t[i+1:]
            else:
                return s[i+1:] ==t[i:]

    return abs(len(s)-len(t))==1