class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res=set()
        for i in range(len(nums)):
            if(nums[i]==key):
                left=0
                right=len(nums)-1
                while(left<=i):
                    if((i-left)<=k):
                        res.add(left)
                    left+=1
                while(i<=right):
                    if(right-i<=k):
                        res.add(right)
                    right-=1
        return sorted(list(res))
