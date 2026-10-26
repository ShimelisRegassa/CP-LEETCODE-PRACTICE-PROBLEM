class Solution:
    def reverseVowels(self, s: str) -> str:
        num=[a for a in s]
        right=len(s)-1
        left=0
        vowel="aeiouAEIOU"
        while(left<right):
            if(num[left] in vowel  and num[right] in vowel):
                num[left],num[right]=num[right],num[left]
                right-=1
                left+=1
            elif(num[left]in vowel and num[right] not in vowel):
                right-=1
            elif(num[left] not in vowel and num[right]  in vowel):
                left+=1
            else:
                right-=1
                left+=1
        return "".join(num)