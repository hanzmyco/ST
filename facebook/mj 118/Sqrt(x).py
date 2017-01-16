def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    start = 1
    end = x
    while start < end - 1:
        mid = (start + end) / 2
        if mid * mid <= x:
            start = mid
        else:
            end = mid
    if end * end <= x:
        return int(end)
    return int(start)