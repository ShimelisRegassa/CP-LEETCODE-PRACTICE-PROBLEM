import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        num=list(itertools.permutations(nums))
        return num