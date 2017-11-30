def canPartitionKSubsets(nums,k):
    total=sum(nums)
    if k<=0 or total%k!=0:
        return False
    visited=[0]*len(nums)
    return canPartition(nums,visited,0,k,0,0,total/k)

def canPartition(nums,visited,start_index,k,cur_sum,cur_num,target):
    if k==1:
        return True
    if cur_sum==target and cur_num>0:
        return canPartition(nums,visited,0,k-1,0,0,target)
    for i in range(start_index,len(nums)):
        if visited[i]==0:
            visited[i]=1
            if canPartition(nums,visited,i+1,k,cur_sum+nums[i],cur_num+1,target):# whether it succeed after consuming num[i]
                return True
    return False