def moveZeros(nums):
    y=0
    for x in xrange(0,len(nums)):
        if nums[x]:
            if nums[x]!=nums[y]:
                nums[x], nums[y] = nums[y],nums[x]
            y+=1
    print nums

def two_pointers(nums):
    left=0
    right=0
    while right< len(nums):
        if nums[right]==1:
            temp=nums[right]
            nums[right]=nums[left]
            nums[left]=temp
            left+=1
        right+=1
    print nums



nums=[0,1,0,3,12]
#moveZeros(nums)
two_pointers(nums)