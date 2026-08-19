class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        right=0
        left=0
        val=1
        counter=0
        while(right<len(nums) and left<len(nums)):
            val*=nums[right]
            while(val>=k and left<len(nums)):
                val/=nums[left]
                left+=1
            counter+=(right-left+1)
            right+=1
        return counter

        