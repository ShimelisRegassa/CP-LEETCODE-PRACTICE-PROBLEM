class Solution:
    def countAnagrams(self, s: str) -> int:
        res=1
        for i in s.split():
            n=len(i)
            counter=Counter(i)
            way=math.factorial(n)
            for  j in counter:
                way//=math.factorial(counter[j])
            res*=way
        return res%(10**9+7)
        



        
