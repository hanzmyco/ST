class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def insert_intervals(intervals, newInterval):
    if newInterval==None:
        return intervals
    insert_position=0
    output=[]
    for ite in intervals:
        if ite.end <newInterval.start:
            insert_position+=1
            output.append(ite)
        elif ite.start > newInterval.end:
            output.append(ite)
        else:
            newInterval.start=min(newInterval.start,ite.start)
            newInterval.end=max(newInterval.end,ite.end)

    output.add(insert_position,newInterval)
    return output
