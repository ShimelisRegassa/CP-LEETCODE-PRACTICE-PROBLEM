class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        res=[]
        count=Counter(nums)
        for i in range(len(nums)):
            if(nums[i]%2==0):
                res.append(nums[i])
    
        for j in nums:
            if(j not in res or res.count(j)<count[j]):
                res.append(j)
        return res
    
            
        
        

        