def search(self, nums, target):
    start = 0
    end = len(nums) - 1
    while start < end - 1:
        middle = start + (end - start) / 2
        if target == nums[middle]:
            return middle
        else:
            if nums[start] < nums[middle]:
                if nums[start] <= target <= nums[middle]:
                    end = middle
                else:
                    start = middle
            else:
                if nums[middle] <= target <= nums[end]:
                    start = middle
                else:
                    end = middle
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end