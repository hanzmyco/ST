def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = [1]
    for i in xrange(1, len(nums)):
        res.append(res[i - 1] * nums[i - 1])
    right = 1
    for i in xrange(len(nums) - 1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res