class Solution:
    def largestOddNumber(self, num: str) -> str:
        m=-1
        for j in range(len(num)-1,-1,-1):
            if(int(num[j])%2==1):
                m=j
                break
            else:
                continue
        if(m!=-1):
            return num[:m+1]
        else:
            return ""

        
        