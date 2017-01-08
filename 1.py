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
        print (i,i+2)
        if A[i] + A[i + 2] == 2 * A[i + 1]:
            dp[(i, i + 2)] = 1
            num += 1
            print num
        else:
            dp[(i, i + 2)] = 0

    for i in xrange(0,lent-3):
        for l in xrange(4,lent-i+1):
            if dp[(i,i+l-2)]==0:
                break
            elif A[i + l - 1] - A[i] == (A[i + 1] - A[i]) * (l - 1):
                    dp[(i, i + l - 1)] = 1
                    num += 1
                    print num
            else:
                    dp[(i, i + l - 1)] = 0
                    break



    return num

input=[1,2,3,4,5,6]
numberOfArithmeticSlices(input)