class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        val=0
        ob={0:1}
        counter=0
        for i in range(len(nums)):
            val+=nums[i]
            if(val-goal in ob):
                counter+=(ob[val-goal])
            ob[val]=ob.get(val,0)+1
        return counter
        