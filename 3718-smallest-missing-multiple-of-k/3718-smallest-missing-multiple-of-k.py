class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        val=0
        for i in range(k,max(nums)+1,k):
            if(i in nums):
                val=i
            else:
                return i
        return val+k