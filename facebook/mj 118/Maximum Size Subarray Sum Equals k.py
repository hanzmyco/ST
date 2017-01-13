def maxSubArrayLen(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    s = 0
    map = {}
    res = 0
    for i in xrange(0, len(nums)):
        s += nums[i]
        if s == k:
            res = i + 1
        elif s - k in map:
            res = max(res, i - map[s - k])
        if s not in map:
            map[s] = i
    return res