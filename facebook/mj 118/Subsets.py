def subsets(nums):
    l=pow(2,len(nums))
    output=[[]]
    for i in xrange(1,l):
        li=[]
        for index in xrange(0,len(nums)):
            if i >> index & 1 ==1:
               li.append(nums[index])
        output.append(li)
    print output

subsets([1,2,3])