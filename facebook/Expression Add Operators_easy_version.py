def leading_zero(num):
    return num.startswith('00') or int(num) and num.startswith('0')   # avoid 00 to 09
def recur(num,target):
    ans=[]
    if leading_zero(num):
        pass
    elif int(num)==target:
        ans.append(num)
    for x in xrange(0,len(num)-1):
        leftnum, rightnum =num[:x+1],num[x+1:]
        if leading_zero(rightnum):
            continue
        for left in recur(leftnum, target-int(rightnum)):
            ans.append(left+'+'+rightnum)
        for left in recur(leftnum, target+int(rightnum)):
            ans.append(left+'-'+rightnum)
    return ans


num='1234567'
target=5
num1='12'
target1=3
print (recur(num,target))

