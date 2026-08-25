class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            if(i!=len(nums)-1):
                val=len(set(nums[:i+1]))-len(set(nums[i+1:]))
                res.append(val)
            else:
                val=len(set(nums[:i+1]))
                res.append(val)
        return res
