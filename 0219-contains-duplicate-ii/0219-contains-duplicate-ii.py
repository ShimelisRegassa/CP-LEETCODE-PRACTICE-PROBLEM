class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        data={}
        for i in range(len(nums)):
            val=i
            if(nums[val]in data and (i-data[nums[val]])<=k):
                return True
            data[nums[i]]=i
        return False

        
        