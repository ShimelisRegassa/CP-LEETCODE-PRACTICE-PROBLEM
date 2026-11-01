class Solution:
    def minMoves(self, nums: list[int]) -> int:
        total=0
        val=min(nums)
        for i in nums:
            total+=abs(i-val)
        return total