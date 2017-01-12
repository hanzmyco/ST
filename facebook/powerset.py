'''
Set  = [a,b,c]
power_set_size = pow(2, 3) = 8
Run for binary counter = 000 to 111

Value of Counter            Subset
    000                    -> Empty set
    001                    -> a
    011                    -> ab
   100                     -> c
   101                     -> ac
   110                     -> bc
   111                     -> abc

 loop counter through 0 to number of powerset
    loop j through set size:
        if counter & (1<<j):
            print set[j]
'''

set=['a','b','c']
total_num=pow(2,len(set))
output=[]
for count in xrange(0,total_num):
    res=''
    for j in xrange(0,len(set)):
        if count & 1<<j:
            res+=set[j]
    output.append(res)
print output
