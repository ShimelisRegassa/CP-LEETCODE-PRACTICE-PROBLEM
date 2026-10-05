class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        if(k>sum(candies)):
            return 0
        left=1
        right=max(candies)
        ans=0
        while(left<=right):
            mid=(left+right)//2
            current=0
            for i in candies:
                current+=(i//mid)
            if(current>=k):
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans
            
         