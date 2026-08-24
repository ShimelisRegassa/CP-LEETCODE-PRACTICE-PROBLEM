class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x:(-len(x),x))
        for i in dictionary:
            left=0
            right=0
            boolean=False
            res=0
            while(right<len(s) and left<len(i)):
                if(s[right]==i[left]):
                    left+=1
                    right+=1
                else:
                    right+=1
                if(left==len(i)):
                    res=i
                    boolean=True
                    break
            if(boolean):
                return res              
        return ""



