# -*- coding: utf-8 -*-
'''
第二种方法intuitive一点

'''

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


def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res, left = 0, 0
        num_map = {}
        l = 0
        for index, ite in enumerate(s):
            if ite not in num_map:
                l += 1
                num_map[ite] = 1
            else:
                num_map[ite] += 1
            while l > k:
                if num_map[s[left]] == 1:
                    del (num_map[s[left]])
                    l -= 1
                else:
                    num_map[s[left]] -= 1
                left += 1
            res = max(res, index - left + 1)
        return res