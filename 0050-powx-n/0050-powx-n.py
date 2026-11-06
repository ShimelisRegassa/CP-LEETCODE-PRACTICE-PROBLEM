class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if(n==1):
                return x
            return x*power(x,n-1)
        return pow(x,n)

        