class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        res=[]
        v=set(nums)
        for i in range(1,len(nums)+1):
            if i not in v:
                res.append(i)
        return res