import itertools
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        for p in  itertools.permutations(nums):
            val=list(p)
            if val not in res:
                res.append(val)
        return res

        