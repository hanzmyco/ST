
def random_pick(nums,target):
    li=[]
    cnt=0
    res=-1
    for ite in nums:
        if ite >target:
            continue
        cnt+=1
        if random.randint(0,cnt-1)==0:
            res=ite
    return res