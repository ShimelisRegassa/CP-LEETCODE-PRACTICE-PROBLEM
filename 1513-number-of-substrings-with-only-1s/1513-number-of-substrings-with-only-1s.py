class Solution:
    def numSub(self, s: str) -> int:
        right=0
        res=0
        while(right<len(s)):
            if(s[right]=="1"):
                left=right+1
                while(left<len(s) and s[left]=="1"):
                    left+=1
                n=(left-right)
                res+=(n*(n+1)//2)
                right=left
                left=0
            else:
                right+=1
        return res%(10**9 +7)

            
                


                
               
                