# -*- coding: utf-8 -*-
'''
循环的写法：先sort，然后每次检查当前值与上一个值是不是一样，如果不一样，那么可以从0开始
每个集合都添加当前值，如果一样，那么就是从上一个（几个）与当前值一样的开始添加
'''

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
nums=[1,2,2]
print iterate(nums)