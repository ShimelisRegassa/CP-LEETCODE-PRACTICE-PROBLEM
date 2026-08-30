class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left=0
        counter=0
        right=0
        if(len(s)==0):
            return True
        while(right<len(t)):
            if(t[right]==s[left]):
                left+=1
                counter+=1
            if(counter==len(s)):
                return True
            right+=1
        return False

        
    