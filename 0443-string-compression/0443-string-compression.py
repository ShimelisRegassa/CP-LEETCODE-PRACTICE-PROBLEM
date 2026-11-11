class Solution:
    def compress(self, chars: list[str]) -> int:
        left=0
        s=""
        b=len(chars)
        if(b==1):
            return b
        for i in range(1,len(chars)):
            if chars[i]==chars[i-1]:
                continue
            else:
                v=i-left
                if(v>1):
                    s+=(chars[left]+str(v))
                else:
                    s+=chars[left]
                left=i
        v=b-left
        if(v>1):
            s+=(chars[left]+str(v))
        else:
            s+=chars[left] 
        right=0
        for i in range(len(s)):
            chars[right]=s[i]
            right+=1
        return len(s)
        
    


            
        
        