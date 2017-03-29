# -*- coding: utf-8 -*-
'''
divisor不断*2,到它+1>dividend 的时候

'''

def divide(dividend, divisor):
    large=dividend
    small=divisor
    i=1
    while large >=small:
        i=1
        while


    while large  >= (small<<i):
        i+=1
    remain=large-(small<<(i-1))
    print i,remain
    if remain>=small:
        return (1<<(i-1))+1
    else:
        return 1<<(i-1)

#print divide(26,3)
#print divide(24,3)
print divide(30,3)

