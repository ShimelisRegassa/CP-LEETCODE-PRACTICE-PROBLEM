class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res=[]
        curr=[]
        def backtrack(start):
            res.append(curr[:]) 
            for i in range(start,len(nums)):
                curr.append(nums[i])
                backtrack(i+1)
                curr.pop()
        backtrack(0)
        return res

        