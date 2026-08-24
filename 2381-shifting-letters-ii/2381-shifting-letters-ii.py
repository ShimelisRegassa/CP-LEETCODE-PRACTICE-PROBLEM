class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff=[0]*(len(s)+1)
        res=[0]*len(s)
        for x,y,z in shifts:
            if(z==0):
                diff[x]-=1
                diff[y+1]+=1
            else:
                diff[x]+=1
                diff[y+1]-=1
        total=0
        for i in range(len(s)):
            total+=diff[i]
            res[i]=total
        final=""
        for i in range(len(s)):
            val=res[i]%26
            new=(ord(s[i])-97+val)%26 +97
            final+=chr(new)
        return final

