class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix=[0]*len(arr)
        prefix[0]=arr[0]
        for i in range(1,len(arr)):
            prefix[i]=prefix[i-1]+arr[i]
        total=0
        even=0
        odd=0
        for j in prefix:
            if(j%2==1):
                total+=(even+1)
                odd+=1
            else:
                total+=(odd)
                even+=1
        return total%(10**9 +7)


            

            
        
        