import random
class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        cnt = 0
        res = -1
        for i in xrange(0, len(self.nums)):
            if self.nums[i] != target:
                continue
            cnt += 1
            if random.randint(0, cnt - 1) == 0:
                res = i
        return res
