def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    res = 100000
    left = 0
    summ = 0
    for i in xrange(0, len(nums)):
        summ += nums[i]
        while left <= i and summ >= s:
            res = min(i - left + 1, res)
            summ -= nums[left]
            left += 1
    if res == 100000:
        return 0
    return res