def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    map = {}
    for ite in wordDict:
        if len(ite) not in map:
            map[len(ite)] = set()
        map[len(ite)].add(ite)
    dp = [True]
    for i in xrange(1, len(s) + 1):
        dp.append(False)
    for i in xrange(0, len(s) + 1):
        for j in xrange(0, i):
            if dp[j] and i - j in map and s[j:i] in map[i - j]:
                dp[i] = True
                break
    return dp[len(s)] 