class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count=Counter(nums)
        total=0
        for i in count:
            v=math.factorial(count[i])
            ch=math.factorial(2)
            d=math.factorial(abs(count[i]-2))
            total+=(v//(ch*d))
        return total

        