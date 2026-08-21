class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        val=""
        n=len(s)
        for j in range(1,n+1):
            if(n%(j)==0):
                sub=s[:j]*(n//j)
                if(s==sub and len(s[:j])!=n):
                    return True
        return False
            



        