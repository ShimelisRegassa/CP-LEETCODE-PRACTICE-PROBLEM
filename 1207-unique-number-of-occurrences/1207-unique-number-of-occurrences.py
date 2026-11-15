class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count=Counter(arr)
        val=0
        fir=0
        lis=list(count.values())
        lis.sort()
        for i in range(1,len(lis)):
            if(lis[i]==lis[i-1]):
                return False
        return True

            
        
        