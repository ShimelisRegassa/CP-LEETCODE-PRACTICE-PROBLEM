class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        right=0
        left=0
        m=0
        n=0
        length1=0
        length2=0
        l=0
        r=0
        while(right<len(answerKey)):
            if(answerKey[right]=="T"):
                m+=1
            while(m>k):
                if(answerKey[left]=="T"):
                    m-=1
                left+=1
            length1=max(length1,right-left+1)
            right+=1
        while(r<len(answerKey)):
            if(answerKey[r]=="F"):
                n+=1
            while(n>k):
                if(answerKey[l]=="F"):
                    n-=1
                l+=1
            length2=max(length2,r-l+1)
            r+=1
        return max(length1,length2)
