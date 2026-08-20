class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        num1=sorted(t)
        num2=sorted(s)
        if(num1==num2):
            return True
        else:
            return False
        