def moveZeros(nums):
    y=0
    for x in xrange(0,len(nums)):
        if nums[x]:
            nums[x], nums[y] = nums[y],nums[x]
            y+=1
    print nums

nums=[0,1,0,3,1,2]
moveZeros(nums)