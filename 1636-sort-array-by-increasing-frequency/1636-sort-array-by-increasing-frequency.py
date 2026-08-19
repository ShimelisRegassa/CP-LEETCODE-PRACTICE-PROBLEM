class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        ob=Counter(nums)
        dictionary=dict(sorted(ob.items(),key=lambda x:(x[1],-x[0])))
        res=[]
        for key,value in dictionary.items():
            for j in range(value):
                res.append(key)
        return res
        
        
