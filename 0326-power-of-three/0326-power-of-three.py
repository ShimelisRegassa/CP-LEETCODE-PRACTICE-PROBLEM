class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        b=n
        p=0
        while(n>=3):
            n//=3
            p+=1
        if(3**p==b):
            return True
        return False