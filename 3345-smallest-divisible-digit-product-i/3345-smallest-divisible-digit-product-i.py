class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        b=str(n)
        while(int(b)>=n):
            val=1
            for i in b:
                val*=int(i)
            if(val%t==0):
                return int(b)
            else:
                b=str(int(b)+1)
    
        