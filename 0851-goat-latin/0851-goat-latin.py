class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        num=sentence.split()
        vowel="aeiouAEIOU"
        for i in range(len(num)):
            if(num[i][0] in vowel):
                num[i]=num[i]+"ma"+"a"*(i+1)
            else:
                temp=num[i][1:]+num[i][0]+"ma"+("a"*(i+1))
                num[i]=temp
        return " ".join(num)

        