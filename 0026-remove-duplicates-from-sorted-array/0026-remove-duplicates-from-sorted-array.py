class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        right=1
        left=0
        while(right<len(nums)):
            if(nums[right]!=nums[left]):
                left+=1
                nums[left]=nums[right]
            right+=1
        return len(set(nums))
      


       