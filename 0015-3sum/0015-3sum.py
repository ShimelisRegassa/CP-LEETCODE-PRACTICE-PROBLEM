class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res=[]
        nums.sort()
        b=len(nums)
        for i in range(len(nums)):
            if(i!=0 and nums[i-1]==nums[i]):
                continue
            left=i+1
            right=b-1
            val=-nums[i]
            while(left<right):
                if(nums[left]+nums[right]<val):
                    left+=1
                elif(nums[left]+nums[right]>val):
                    right-=1
                else:
                    res.append([nums[left],nums[right],-val])
                    right-=1
                    left+=1
                    while(right>-1 and nums[right]==nums[right+1]):
                        right-=1
                    while(left>b and nums[left]==nums[left-1]):
                        left-=1
        return res           
        

    
   
        
        
            


        