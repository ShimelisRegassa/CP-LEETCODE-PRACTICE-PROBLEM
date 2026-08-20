class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        data=[]
        nums.sort()
        for i in range(len(nums)):
            if(nums[i]==target):
                data.append(i)
        return data

