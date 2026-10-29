class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        num=set(nums)
        res=[]
        for x in num:
            if(x>0):
                res.append(x)
        res.sort()
        for i in range(1,len(res)+1):
            if(res[i-1]!=i):
                return i
        if(len(res)!=0):
            return max(res)+1
        else:
            return 1
        