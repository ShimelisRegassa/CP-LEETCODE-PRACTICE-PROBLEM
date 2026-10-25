class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        right=0
        left=0
        count={}
        fre=0
        counter=0
        while(right<len(s)):
            count[s[right]]=count.get(s[right],0)+1
            fre=max(fre,count[s[right]])
            while((right-left+1)-fre>k):
                count[s[left]]-=1
                if(count[s[left]]==0):
                    del count[s[left]]
                left+=1
            counter=max(counter,right-left+1)
            right+=1
        return counter
        
       


        


