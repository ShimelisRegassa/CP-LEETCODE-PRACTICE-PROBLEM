class Solution:
    def sortColors(self, nums: List[int]) -> None:

        num=len(nums)
        for i in range(num):

            for j in range(num-1):
                if(nums[j]>nums[j+1]):
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        print (nums)
        