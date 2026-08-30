class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        val=0
        total=sum(nums)
        counter=0
        for i in range(len(nums)-1):
            val+=nums[i]
            if(val>=total-val):
                counter+=1
        return counter

                

  
        