class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        b=n
        v=0
        while(n>=2):
            n//=2
            v+=1
        if(2**v==b):
            return True
        return False