def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if len(needle) == 0:
        return 0
    m = len(haystack)
    n = len(needle)
    if m < n:
        return -1
    position = []
    for i in xrange(0, m - n + 1):
        if haystack[i] == needle[0]:
            position.append(i)
    for i in position:
        j = 0
        while j<n:
            if haystack[i + j] != needle[j]:
                break
            j+=1
        if j == n:
            return i
    return -1

print strStr('a','a')