def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left = 0
    right = len(nums) - 1
    if nums[left] > nums[right]:
        while left + 1 < right:
            middle = left + (right - left) / 2
            if nums[left] < nums[middle]:
                left = middle
            else:
                right = middle
        return min(nums[left], nums[right])
    return nums[left]