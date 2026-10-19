class Solution:
    def sortSentence(self, s: str) -> str:
        num=s.split()
        count={}
        for i in num:
            count[int(i[-1])]=i[:-1]
        res=sorted(count.items(),key=lambda x:x[0])
        out=[]
        for x,y in res:
            out.append(y)
        return " ".join(out)
        
        
        




        