import sys
def maxSubArray( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = -sys.maxint - 1
    cur_some = 0
    start=0
    end=0
    m_start=0
    m_end=0
    for index, i in enumerate(nums):
        cur_some += i
        cur_some = max(cur_some, i)
        if i==cur_some:
            start=index
        end=index
        res = max(res, cur_some)
        if res ==cur_some:
            m_start=start
            m_end=end
    print res
    print m_start
    print m_end

input=[-2,1,-3,4,-1,2,1,-5,4]
maxSubArray(input)