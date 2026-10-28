class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        nums.sort()
        res=[]
        m=max(nums)
        b=min(nums)
        if(lower>upper):
            return []
        if not nums:
            return [] 
        if(lower<b):
            res.append([lower,min(b-1,upper)])
        for i in range(1,len(nums)):
            if(nums[i]!=nums[i-1] and nums[i]!=nums[i-1]+1):
                fir=max(nums[i-1]+1,lower)
                sec=min(nums[i]-1,upper)
                if(fir<=sec):
                    res.append([fir,sec])
        if(m<upper):
            lef=max(m+1,lower) 
            if(lef<=upper):
                res.append([lef,upper])
        return res
            
        