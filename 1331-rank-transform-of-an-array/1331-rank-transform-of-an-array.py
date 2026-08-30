class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp=set(arr)
        num=sorted(list(temp))
        ob={}
        res=[]
        for i,y in enumerate(num):
            ob[y]=i+1
        for i in arr:
            res.append(ob[i])
        return res
        