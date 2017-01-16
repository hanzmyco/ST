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

def minMeetingRooms(intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        rooms = []
        if len(intervals) == 0:
            return 0

        for index,ite in enumerate(intervals):
            rooms.append((ite[0], 1,index))
            rooms.append((ite[1], 0,index))
        rooms.sort(cmp=cmp1)
        maxx = 0
        num = 0
        output=[]
        for ite in rooms:
            if ite[1] == 1:
                num += 1
                output.append((num,ite[2]))
                maxx = max(maxx, num)
            else:
                num -= 1
        print output
        return maxx


intervals=[[1,2],[3,5],[6,19],[2,3],[7,13]]
print minMeetingRooms(intervals)