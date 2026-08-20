class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data=Counter(nums)
        val=list(data.values())
        out=[]
        val.sort(reverse= True)
        for i in range(k):
            for key,value in data.items():
                if(val[i]==value):
                    if key not in out:
                        out.append(key)
                        break
                    
        return (out)