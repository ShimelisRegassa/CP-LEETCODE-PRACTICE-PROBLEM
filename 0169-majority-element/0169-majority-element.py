class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n=len(nums)//2
        count=Counter(nums)
        for i in nums:
            if(count[i]>n):
                return i


        