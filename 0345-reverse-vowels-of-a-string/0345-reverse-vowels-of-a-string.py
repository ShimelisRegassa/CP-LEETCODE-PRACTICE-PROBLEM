class Solution:
    def reverseVowels(self, s: str) -> str:
        right=len(s)-1
        left=0
        d=[a for a in s]
        m="aeiouAEIOU"
        while(left<right):
            if(d[left] in m and d[right] in m):
                d[left],d[right]=d[right],d[left]
                left+=1
                right-=1
            elif(d[left] in m and d[right]  not in m):
                right-=1
            else:
                left+=1
        return "".join(d)


        