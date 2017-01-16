import sys
def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    m1 = sys.maxint
    m2 = sys.maxint
    for ite in nums:
        if ite <= m1:
            m1 = ite
        elif ite <= m2:
            m2 = ite
        else:
            return True
    return False