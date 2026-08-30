class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        num=[]
        for i in nums:
            num.append(i*i)
        return sorted(num)
        