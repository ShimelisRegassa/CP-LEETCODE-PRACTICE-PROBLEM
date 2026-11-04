class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        counter=0
        num=1
        for i in range(1,len(s)):
            if(ord(s[i])==ord(s[i-1])+1):
                num+=1
            else:
                counter=max(counter,num)
                num=1
        counter=max(counter,num)
        return counter