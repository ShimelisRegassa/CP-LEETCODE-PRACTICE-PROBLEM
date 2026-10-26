class Solution:
    def possibleStringCount(self, word: str) -> int:
        counter=1
        for i in range(len(word)-1):
            if(word[i]==word[i+1]):
                counter+=1
        return counter

        


        