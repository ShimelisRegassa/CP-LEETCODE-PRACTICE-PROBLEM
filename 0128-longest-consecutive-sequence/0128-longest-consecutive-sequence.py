class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique=set(nums)
        
        length=0
        for i in unique:
            if( i-1 not in unique):
                element=i
                count=1
                while element+1 in unique:
                    element+=1
                    count+=1
                length =max(length,count) 
        return length


            
        