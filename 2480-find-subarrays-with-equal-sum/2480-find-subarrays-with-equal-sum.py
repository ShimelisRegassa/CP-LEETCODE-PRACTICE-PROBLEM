class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        check=set()
        for j in range(len(nums)-2+1):
            summation=sum(nums[j:j+2])
            if(summation in check):
                return True
            else:
                check.add(summation)
        return False