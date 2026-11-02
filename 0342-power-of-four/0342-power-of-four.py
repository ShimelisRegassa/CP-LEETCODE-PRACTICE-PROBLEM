class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        p=n
        c=0
        while(n>=4):
            n//=4
            c+=1
        if(4**c==p):
            return True
        return False