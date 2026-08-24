class Solution:
    def maxPower(self, s: str) -> int:
        counter=1
        maximum=1
        for i in range(1,len(s)):
            if(s[i]==s[i-1]):
                counter+=1
            else:
                counter=1
            maximum=max(maximum,counter)
        return maximum
        