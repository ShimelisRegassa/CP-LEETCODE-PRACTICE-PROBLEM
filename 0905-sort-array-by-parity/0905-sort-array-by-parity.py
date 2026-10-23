class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        res=[]
        val=[]
        count=Counter(nums)
        for i in range(len(nums)):
            if(nums[i]%2==0):
                res.append(nums[i])
            else:
                val.append(nums[i])
        res.extend(val)
        return res
    
            
        
        

        