class Solution:
    def countValidPrefixes(self, s: str) -> int:
        b=0
        for i in range(len(s)):
            c=s[:i+1]
            m=c.count("1")
            n=c.count("0")
            if(abs(m-n)==0 and len(c)%2==0 or abs(m-n)==1and      len(c)%2==1):
                b+=1
                
        return b
        