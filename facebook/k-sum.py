def recur(num,k,target):
    if k > 1:
        for index in xrange(0, len(num)):
            if recur(num[:index] + num[index + 1:], k - 1,target - num[index]):
                return True

    else:
        if num[0] ==target:
            return True
    return False
def ksum(num,k,target):
    num.sort()
    return recur(num,k,target)

num=[2,3,1,5,6]
print ksum(num,4,14)