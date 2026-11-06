class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        p=""
        for i in b:
            p+=(str(i))
        p=int(p)
        def power(a,p):
            if(p==0):
                return 1
            half=power(a,p//2)
            if(p%2==0):
                return (half*half)%1337
            else:
                return (a*half*half)%1337
        return power(a,p)%1337

        