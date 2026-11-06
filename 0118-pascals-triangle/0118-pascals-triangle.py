class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        def pascal(n):
            if n==1:
                return [1]

            prev=pascal(n-1)
            row=[1]
            for i in range(1,n-1):
                row.append(prev[i-1]+prev[i])
            row.append(1)
            return row
        res=[]
        for i in range(1,numRows+1):
            res.append(pascal(i))
        return res
        

