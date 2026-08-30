class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        num=[0]*len(nums)
        total=0
        for i in range(len(nums)):
            num[i]=total
            total+=nums[i]
        for i in range(len(num)):
            if(num[i]==total-num[i]-nums[i]):
                return i
        return -1

       
           