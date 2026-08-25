class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        res=[]
        check1=set()
        check2=set()
        num1=[0]*len(nums)
        num2=[0]*len(nums)
        val1=0
        val2=0
        for i in range(len(nums)):
            if(nums[i] not in check1):
                check1.add(nums[i])
                val1+=1
            num1[i]=val1
        for j in range(len(nums)-2,-1,-1):
            if(nums[j+1] not in check2):
                val2+=1
                check2.add(nums[j+1])
            num2[j]=val2
        for i in range(len(nums)):
            res.append(num1[i]-num2[i])
        return res

            
        
