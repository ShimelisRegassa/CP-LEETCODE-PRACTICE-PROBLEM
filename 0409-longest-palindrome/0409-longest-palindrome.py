class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter=Counter(s)
        res=0
        for i in counter:
            if(counter[i]%2==0):
                res+=counter[i]
            else:
                res+=counter[i]-1
        if(res<len(s)):
            res+=1
        return res