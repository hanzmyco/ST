def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    l = 0
    r = 0
    for ite in nums:
        l = max(l, ite)
        r += ite
    while l < r:
        mid = l + (r - l) / 2
        if self.can_split(nums, m, mid):
            r = mid
        else:
            l = mid + 1
    return l


def can_split(nums, m, ssum):
    cnt = 1
    curSum = 0
    for i in xrange(0, len(nums)):
        curSum += nums[i]
        if curSum > ssum:
            curSum = nums[i]
            cnt += 1
            if cnt > m:  # ssum定的太小，所以l=mid_1
                return False
    return True