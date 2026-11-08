class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        if(len(nums)%2==0):
            target=nums[(len(nums)//2)-1]
            counter=0
            for i in nums:
                counter+=(abs(i-target))
            return counter
        else:
            target=nums[len(nums)//2]
            counter=0
            for i in nums:
                counter+=(abs(i-target))
            return counter
            
















        5
      
            
