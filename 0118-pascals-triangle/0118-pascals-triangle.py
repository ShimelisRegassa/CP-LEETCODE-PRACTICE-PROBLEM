class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res=[]
        for j in range(1,numRows+1):
            v=math.factorial(j-1)
            lst=[]
            for i in range(j):
                t=math.factorial(i)
                m=math.factorial(j-i-1)
                temp=v//(t*m)
                lst.append(temp)
            res.append(lst)
        return res  


