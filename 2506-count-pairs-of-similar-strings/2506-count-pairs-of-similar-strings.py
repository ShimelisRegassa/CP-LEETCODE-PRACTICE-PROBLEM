class Solution:
    def similarPairs(self, words: List[str]) -> int:
        counter=0
        for j in  range(len(words)-1):
            for k in range(j+1,len(words)):
                if(set(words[j])==set(words[k])):
                    counter+=1
        return counter

        