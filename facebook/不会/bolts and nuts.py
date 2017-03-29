# -*- coding: utf-8 -*-
'''
快排的思想
'''

def partition(arr,low,high,pivot):
    i=low
    j=low
    while j<high:
        if arr[j] < pivot:
            swap(arr,i,j)
            i+=1
        elif arr[j]==pivot:
            swap(arr,j,high)
            j-=1
        j+=1
    swap(arr,i,high)
    return i
def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

def matchPairs(nuts,bolts,low,high):
    if low >=high:
        return
    pivot=partition(nuts,low,high,bolts[high])
    partition(bolts,low,high,nuts[pivot])
    matchPairs(nuts,bolts,low,pivot-1)
    matchPairs(nuts,bolts,pivot+1,high)