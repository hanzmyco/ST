from heapq import *
# -*- coding: utf-8 -*-
'''
 最大堆存小的那一半，最小堆存大的那一半, 最小堆得长度》=最大堆得长度
'''
class MedianFinder(object):
    def __init__(self):
        self.heaps=[],[]
    def addNum(self,num):
        small,large=self.heaps
        heappush(small, -heappushpop(large,num))  #最大堆是取反
        if len(large)<len(small):
            heappush(large,-heappop(small))
    def findMedian(self):
        small, large = self.heaps
        if len(large)>len(small):
            return float(large[0])
        return (large[0]-small[0])/2.0