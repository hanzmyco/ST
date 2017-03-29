# -*- coding: utf-8 -*-
'''
要确认insert的位置
遍历每个区间，如果ite.end < new.start，那么insert_position+=1
如果ite.start > newInterval.end,那么就把这个插入output,
然后后面全部插入就行。如果不是上面两者，那么就更新小的和大的

'''


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def insert_intervals(intervals, newInterval):
    if newInterval == None:
        return intervals
    insert_position = 0
    l = len(intervals)
    i = 0
    while i < l:
        ite = intervals[i]
        if ite.end < newInterval.start:
            insert_position += 1
        elif ite.start > newInterval.end:
            break
        else:
            newInterval.start = min(newInterval.start, ite.start)
            newInterval.end = max(newInterval.end, ite.end)
            intervals.pop(i)
            i -= 1
            l -= 1
        i += 1
    intervals.insert(insert_position, newInterval)
    return intervals