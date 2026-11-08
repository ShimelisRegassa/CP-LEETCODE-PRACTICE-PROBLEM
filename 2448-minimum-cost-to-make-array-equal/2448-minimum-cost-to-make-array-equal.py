class Solution:
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        nums=sorted(zip(nums,cost))
        total=sum(cost)
        target=0
        counter=0
        for i,y in nums:
            target+=y
            if(target*2>=total):
                target=i
                break
        for i,y in nums:
            dif=abs(i-target)
            if(dif>0):
                counter+=(y*dif)
        return counter
    
              