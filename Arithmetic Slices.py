def numberOfArithmeticSlices(A):
    """
    :type A: List[int]
    :rtype: int
    """
    dp = {}
    num = 0
    lent = len(A)
    if lent < 3:
        return 0
    for i in xrange(0, lent - 2):
        if A[i] + A[i + 2] == 2 * A[i + 1]:
            dp[(i, i + 2)] = 1
            num += 1
        else:
            dp[(i, i + 2)] = 0
    for l in xrange(4, lent + 1):
        for i in xrange(0, lent - l + 1):
            if dp[(i, i + l - 2)] == 1:
                if A[i + l - 1] - A[i] == (A[i + 1] - A[i]) * (i + l - 1):
                    dp[(i, i + l - 1)] = 1
                    num += 1
                else:
                    dp[(i, i + l - 1)] = 0
            else:
                dp[(i, i + l - 1)] = 0
    return num
