class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        right=0
        left=0
        counter=0
        count=Counter()
        n=len(s)
        while(right<len(s)):
            count[s[right]]+=1
            while(len(count)==3):
                counter+=(n-right)
                count[s[left]]-=1
                if(count[s[left]]==0):
                    del count[s[left]]
                left+=1
            right+=1
        return counter
        