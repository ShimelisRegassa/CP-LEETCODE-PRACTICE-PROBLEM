class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        right=0
        left=0
        b=0
        n=0
        l=0
        r=0
        counter1=0
        counter2=0
        while(right<len(nums)):
            if(nums[right]%2==1):
                b+=1
            while(b>k):
                if(nums[left]%2==1):
                    b-=1
                left+=1
            counter1+=(right-left+1)
            right+=1
        while(r<len(nums)):
            if(nums[r]%2==1):
                n+=1
            while(n>k-1):
                if(nums[l]%2==1):
                    n-=1
                l+=1 
            counter2+=(r-l+1)
            r+=1
        return counter1-counter2

        


        


        