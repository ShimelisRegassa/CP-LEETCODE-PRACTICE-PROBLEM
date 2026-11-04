class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if(len(nums)==0):
            return 0
        nums=list(set(nums))
        nums.sort()
        counter=0
        num=1
        for i in range(1,len(nums)):
            if(nums[i]==nums[i-1]+1):
                num+=1
            else:
                counter=max(counter,num)
                num=1
        counter=max(counter,num)
        return counter
        