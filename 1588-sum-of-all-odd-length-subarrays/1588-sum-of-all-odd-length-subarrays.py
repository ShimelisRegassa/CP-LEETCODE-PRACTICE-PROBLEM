class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total=0
        num=[0]*len(arr)
        val=0
        for i in range(len(arr)):
            val+=arr[i]
            num[i]=val
        for i in range(len(arr)):
            if(i%2==0):
                total+=num[i]
                v=0
                for j in range(i+1,len(num)):
                    total+=(num[j]-num[v])
                    v+=1
        return total


        