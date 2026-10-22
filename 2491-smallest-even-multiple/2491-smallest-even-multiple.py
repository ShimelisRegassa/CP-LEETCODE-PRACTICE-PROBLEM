class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        val=2*n
        for i in range(2,val+1,2):
            if(i%n==0):
                return i
        
        