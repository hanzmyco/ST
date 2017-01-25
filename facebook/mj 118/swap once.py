import collections
def swap_once(nums):
    maxx=[nums[len(nums)-1],len(nums)-1]
    que=[(nums[len(nums)-1],len(nums)-1)]
    for i in xrange(len(nums)-1,-1,-1):
        if nums[i] > maxx[0]:
            maxx=[nums[i],i]
        que.append((nums[i],maxx[0],maxx[1]))
    for i in xrange(len(que)-1,-1,-1):
        if que[i][0] != que[i][1]:
            swap(nums,len(que)-i-1,que[i][2])
            break

    print nums

def swap(nums,i,j):
    temp=nums[i]
    nums[i]=nums[j]
    nums[j]=temp

nums=[4,2,1,3,4]
swap_once(nums)