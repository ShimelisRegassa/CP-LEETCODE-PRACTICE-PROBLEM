class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        counter=0
        while(left<right):
            counter=max(counter,nums[right]+nums[left])
            left+=1
            right-=1
        return counter

        
        