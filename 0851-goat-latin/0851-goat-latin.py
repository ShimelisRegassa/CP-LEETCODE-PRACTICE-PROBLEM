class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        num=sentence.split()
        vowel="aeiouAEIOU"
        c=1
        result=""
        for i in num:
            if i[0] in vowel:
                result+=i+"ma"+"a"*c+" "
            else:
                result+=i[1:]+i[0]+"ma"+"a"*c+" "
            c+=1
        return result.strip()


        