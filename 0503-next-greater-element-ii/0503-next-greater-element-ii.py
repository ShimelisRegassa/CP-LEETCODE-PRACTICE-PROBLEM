class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        stack=[]
        check={}
        for i in range(n*2):
            index=i%n
            while(stack and nums[stack[-1]]<nums[index]):
                val=stack.pop()
                res[val]=nums[index]
            if(i<n):
                stack.append(i)
        return res




        