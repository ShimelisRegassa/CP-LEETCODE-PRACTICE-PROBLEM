class Solution:
    def partitionString(self, s: str) -> int:
        right=0
        left=0
        count={}
        counter=0
        for i in s:
            count[i]=count.get(i,0)+1
            if(count[i]>1):
                counter+=1
                count.clear()
                count[i]=1
        if(len(count)!=0):
            counter+=1
        return counter