class Solution:
    def countHomogenous(self, s: str) -> int:
        left=0
        right=0
        total=0
        while(right<len(s) and left<len(s)):
            if (s[right]!=s[left]):
                long=right-left
                total+=(long*(long+1)//2)
                left=right
            right+=1
        fin=right-left
        total+=(fin*(fin+1)//2)
        return total%(10**9 +7)
        

            
            
        