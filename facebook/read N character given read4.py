


a='1234567891'
def read4(buf):
    return 0

def read(self, buf, n):
    """
    :type buf: Destination buffer (List[str])
    :type n: Maximum number of characters to read (int)
    :rtype: The number of characters read (int)
    """
    '''
    res=0
    for i in xrange(0,n/4+1):
        cur=read4(buf[res:])
        if cur==0:
            break
        res+=cur
    return min(res,n)
    '''
    t = read4(buf)
    if t >= n:
        return n
    if t < 4:
        return t
    return 4 + self.read(buf[4:], n - 4)

def iteration(buf,n):
    res=0
    for i in xrange(0,n/4+1):
        cur=read4(buf[res:])
        if cur==0:
            break
        res+=cur
    return min(res,n)