class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res=[]
        current=[]
        def backtrack(start):
            if(len(current)==k):
                res.append(current[:])
            for i in range(start,n+1):
                current.append(i)
                backtrack(i+1)
                current.pop()
        backtrack(1)
        return res