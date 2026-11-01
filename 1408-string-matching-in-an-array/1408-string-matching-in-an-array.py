class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        counter=0
        res=[]
        words.sort(key=lambda x:len(x))
        for j  in range(len(words)-1):
            le=0
            w=words[j]
            for i in range(j+1,len(words)):
                m=words[i]
                if(w in m):
                    res.append(w)
        fin=[]  
        for i in res:
            if i not in fin:
                fin.append(i)
        return fin