
def swap(a,i,j):
    temp=a[i]
    a[i]=a[j]
    a[j]=temp
def nextPermutation(nums):
    n=len(nums)
    for i in xrange(len(nums)-2,-1,-1):
        if nums[i+1] > nums[i]:
            for j in xrange(n-1,i-1,-1):
                if nums[j] > nums[i]:  #find the first one that is larger than i
                    print i
                    print j
                    break

            swap(nums,i,j)
            print nums
            nums[i+1:].reverse()
            return
    nums.reverse()


nums=[1,2,7,4,3,1]
nextPermutation(nums)
print nums

