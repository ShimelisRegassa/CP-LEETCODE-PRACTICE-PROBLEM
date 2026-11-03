class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=10**9 +7
        if(n%2==0):
            b=n//2
            total=pow(5,b,mod)* pow(4,b,mod)
        else:
            e=n//2+1
            o=n//2
            total=pow(5,e,mod)* pow(4,o,mod)
        return total%(10**9+7)