from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        data=Counter(s)
        for i ,y in data.items():
            if(y==1):
                return s.index(i)
        return -1