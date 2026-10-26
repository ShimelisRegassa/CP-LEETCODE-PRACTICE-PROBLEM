class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        m=len(s)
        left=0
        i=2*k
        res=""
        while(left+i<=m):
            res+=(s[left:left+k][::-1])
            res+=(s[left+k:left+i])
            left+=i
        if(left+k>=m):
            res+=s[left:left+k][::-1]
        else:
            res+=s[left:left+k][::-1]
            res+=s[left+k:]
        return res

        

            



        