class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        num1=[0]*len(nums)
        num2=[0]*len(nums)
        b=len(nums)
        res=[]
        for i in range(1,b):
            num1[i]=num1[i-1]+nums[i-1]
        for j in range(b-2,-1,-1):
            num2[j]=num2[j+1]+nums[j+1]
        for j in range(len(nums)):
            c=(nums[j]*j -num1[j])+(num2[j]-(b-j-1)*nums[j])
            res.append(c)
        return res
        