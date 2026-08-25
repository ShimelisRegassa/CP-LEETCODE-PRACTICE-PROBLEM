class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        val=float("inf")
        res=[]
        for i in range(1,len(arr)):
            val=min(val,arr[i]-arr[i-1])
        for i in range(1,len(arr)):
            if(arr[i]-arr[i-1]==val):
                res.append([arr[i-1],arr[i]])
        return res



        