# -*- coding: utf-8 -*-
'''
这题关键是delete insert in O(1),其实就是用dic来存 值得位置，用array来存真正的值
删除的时候就把该值换到最后，然后删掉最后就行了
'''

def __init__(self):
    """
    Initialize your data structure here.
    """
    self.nums = []
    self.map = {}


def insert(self, val):
    """
    Inserts a value to the set. Returns true if the set did not already contain the specified element.
    :type val: int
    :rtype: bool
    """
    if val in self.map:
        return False
    self.nums.append(val)
    self.map[val] = len(self.nums) - 1
    return True


def remove(self, val):
    """
    Removes a value from the set. Returns true if the set contained the specified element.
    :type val: int
    :rtype: bool
    """
    if val not in self.map:
        return False
    position = self.map[val]
    val2 = self.nums[len(self.nums) - 1]
    self.map[val2] = position
    self.nums[position] = val2
    del self.map[val]
    self.nums.pop()
    return True


def getRandom(self):
    """
    Get a random element from the set.
    :rtype: int
    """
    if len(self.nums) == 0:
        return None
    if len(self.nums) == 1:
        return self.nums[0]
    index = random.randint(1, len(self.nums) - 1)
    return self.nums[index]