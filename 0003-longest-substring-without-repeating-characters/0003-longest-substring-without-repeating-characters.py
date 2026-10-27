class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right=0
        left=0
        count={}
        counter=0
        while(right<len(s)):
            count[s[right]]=count.get(s[right],0)+1
            while(count[s[right]]>1):
                count[s[left]]-=1
                if(count[s[left]]==0):
                    del count[s[left]]
                left+=1
            counter=max(counter,right-left+1)
            right+=1
        return counter

    

        


       
                
        