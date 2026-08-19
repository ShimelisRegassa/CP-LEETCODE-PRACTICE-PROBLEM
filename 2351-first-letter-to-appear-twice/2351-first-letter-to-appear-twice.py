class Solution:
    def repeatedCharacter(self, s: str) -> str:
        ob={}
        for i in (s):
            ob[i]=ob.get(i,0)+1
            if(ob[i]==2):
                return i
        