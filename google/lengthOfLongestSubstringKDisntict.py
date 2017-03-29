def lengthOfLongestSubstringKDistinct(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    res, left = 0, 0
    pos = {}
    for index, ite in enumerate(s):
        pos[ite] = index
        while len(pos) > k:
            if pos[s[left]] == left:
                del (pos[s[left]])
            left += 1
        res = max(res, index - left + 1)
    return res