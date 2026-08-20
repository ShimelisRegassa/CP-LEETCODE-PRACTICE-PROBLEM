class Solution:
    def minSteps(self, s: str, t: str) -> int:
        data1=Counter(s)
        data2=Counter(t)
        count=0
        m=set(s)
        for i in m:
            if  i in t and data1[i]==data2[i]:
                continue
            elif( i in t and data1[i]>data2[i]):
                count+=(data1[i]-data2[i])
            elif(i not in t):
                count+=data1[i]
        return count


        