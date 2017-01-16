import copy
def recur(nums, index, output, current):
    for i in xrange(index, len(nums)):
        if i == index or nums[i] != nums[i - 1]:
            current.append(nums[i])
            output.append(copy.copy(current))
            recur(nums, i + 1, output, current)
            current.pop()

def iterate(nums):
        output = [[]]
        if len(nums) == 0:
            return output
        nums.sort()
        size, last = 1, nums[0]
        for i in xrange(0, len(nums)):
            if last != nums[i]:
                last = nums[i]
                size = len(output)
            new_size = len(output)
            for j in xrange(new_size - size, len(output)):
                output.append(copy.deepcopy(output[j]))
                output[len(output) - 1].append(nums[i])
        return output

def subsetsWithDup(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    output = [[]]
    current = []
    nums.sort()
    recur(nums, 0, output, current)
    return output