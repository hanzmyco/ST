# -*- coding: utf-8 -*-
'''
对单词num以及target进行递归，如果num==target时，把这个东西返回到结果里面
然后对单词的每个index，进行一次分割，分为左边和右边
如果右边是leading zero，就continue
然后开始递归（找到满足leftnum,target +/-右边的所有组合），对所有递归得到的左边值，
ans添加 left+'+'+right
'''

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


num='123400567'
target=5
num1='12'
target1=3
print (recur(num,target))

