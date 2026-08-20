class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        maximum=0
        for j in range(len(nums)-1):
            for k in range(len(nums)):
                val=math.gcd(nums[j],nums[k])
                maximum=max(maximum,(nums[j]*nums[k])//val**2)
        return maximum


        