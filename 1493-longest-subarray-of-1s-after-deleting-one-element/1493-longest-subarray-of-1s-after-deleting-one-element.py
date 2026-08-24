class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        right=0
        left=0
        k=0
        length=0
        while(right<len(nums)):
            if(nums[right]==0):
                k+=1
            while(k>1):
                if(nums[left]==0):
                    k-=1
                left+=1
                
            length=max(length,right-left+1)
            right+=1
       
        return length-1
        

            



        