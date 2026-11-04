class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if(len(nums)<3):
            return 0
        total=0
        counter=0
        for i in range(2,len(nums)):
            if(nums[i]-nums[i-1]==nums[i-1]-nums[i-2]):
                counter+=1
            else:
                counter=0
            total+=counter
        return total
         
        