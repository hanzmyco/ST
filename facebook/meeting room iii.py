# -*- coding: utf-8 -*-
'''
按结束时间排序
'''

def cmp1(m1,m2):
    if m1[1] <m2[1]:
        return -1
    elif m1[1] == m2[1]:
        return m1[0] < m2[1]
    else:
        return 1

def findLargestBefore(i,meetings,dp):  # not attached
    for j in xrange(i-1,-1,-1):
        if dp[j][1] <= meetings[i][0]:
            return j




'''
与上一个相比，dp[j]代表算到第J个为止，所有会议的区间情况以及weight情况
'''

def maxWeight(meetings):
    meetings.sort(cmp1)
    dp=[(meetings[0][0],meetings[0][1],meetings[0][2])]
    for i in xrange(1,len(meetings)):
        begin=0
        end=0
        weight=0
        j=findLargestBefore(i,meetings,dp)
        if i-1==j: #last one is not attached    可以和下面合并
            begin=dp[j][0]
            end=meetings[i][1]
            weight=dp[j][2]+meetings[i][2]
        else:
            if dp[j][2] + meetings[i][2] > dp[i-1][2]:
                begin=dp[j][0]
                end=meetings[i][1]
                weight=dp[j][2] + meetings[i][2]
            else:
                begin=dp[i-1][0]
                end=dp[i-1][1]
                weight=dp[i-1][2]
        dp.append((begin,end,weight))
    return dp[len(meetings)-1][2]

meetings=[(1,2,50),(3,5,20),(6,19,100),(2,100,200)]
print maxWeight(meetings)