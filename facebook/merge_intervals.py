class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e
def cmp1(t1, t2):
    if t1[0] < t2[0]:
        return -1
    elif t1[0] == t2[0]:
        if t1[1] < t2[1]:
            return -1
        elif t1[1] > t2[1]:
            return 1
        else:
            return 0
    else:
        return 1


def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    new_invals = []
    for ite in intervals:
        new_invals.append((ite.start, 0))
        new_invals.append((ite.end, 1))
    new_invals.sort(cmp=cmp1)
    num = 0
    start = 0
    end = 0
    output = []
    for ite in new_invals:
        if num == 0:
            start = ite[0]
            num += 1
        else:
            if ite[1] == 0:
                num += 1
            else:
                num -= 1
                if num == 0:
                    end = ite[0]
                    new_interval = Interval(start, end)
                    output.append(new_interval)
    return output

a=[Interval(1,3)]
output= merge(a)
for ite in output:
    print ite.start
    print ite.end