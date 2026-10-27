from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a=len(s)
        b=len(p)
        num1=[0]*(26)
        num2=[0]*(26)
        res=[]
        for i in s[:b]:
            num1[ord(i)-97]+=1
        for i in p:
            num2[ord(i)-97]+=1
        if(num1==num2):
            res.append(0)
        for i in range(b,a):
            num1[ord(s[i])-97]+=1
            num1[ord(s[i-b])-97]-=1
            if(num1==num2):
                res.append(i-b+1)
        return res
        

