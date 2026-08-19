class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        num1=Counter(ransomNote)
        num2=Counter(magazine)
        for key,value in num1.items():
            if(key not in num2 or(key in num2 and num1[key]>num2[key])):
                return False
            else:
                continue
        return True