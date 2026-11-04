class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if(rowIndex==0):
            return [1 ]
        res=[]
        for i in range(rowIndex+1):
            c=math.factorial(rowIndex)
            val=c//((math.factorial(i))*(math.factorial(rowIndex-i)))
            res.append(val)
        return res