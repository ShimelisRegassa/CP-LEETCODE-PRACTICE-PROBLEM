class Solution:
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        nums=sorted(zip(nums,cost))
        l=len(nums)
        total=sum(cost)
        target=0
        val=0
        for i,y in nums:
            target+=y
            if(target*2>=total):
                target=y
                val=i
                break
        if(l%2==0):
            counter=0
            for i,y in nums:
                dif=abs(i-val)
                if(dif>0):
                    counter+=(y*dif)
            return counter
        else:
            counter=0
            for i,y in nums:
                dif=abs(i-val)
                if(dif>0):
                    counter+=(y*dif)
            return counter
        
              