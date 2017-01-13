def method1(self, s):
    if len(s) == 0:
        return 0
    map = [-1] * 256
    left = 0
    res = 0
    for i in xrange(0, len(s)):
        if map[ord(s[i])] == -1 or map[ord(s[i])] < left:
            res = max(res, i - left + 1)
        else:
            left = map[ord(s[i])] + 1
        map[ord(s[i])] = i
    return res


def method2(self, s):
    if len(s) == 0:
        return 0
    map = {}
    left = 0
    res = 0
    end = 0
    while end < len(s):
        if s[end] not in map or map[s[end]] < left:
            res = max(res, end - left + 1)
        else:
            left = map[s[end]] + 1
        map[s[end]] = end
        end += 1
    return res