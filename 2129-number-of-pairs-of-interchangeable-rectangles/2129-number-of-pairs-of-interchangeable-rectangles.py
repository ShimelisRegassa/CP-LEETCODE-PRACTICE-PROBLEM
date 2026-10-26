class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        count={}
        counter=0
        res=0
        for i in rectangles:
            count[i[0]/i[1]]=count.get(i[0]/i[1],0)+1
        for i in count:
            val=count[i]
            v=math.factorial(val)
            res+=v//(2*(math.factorial(abs(val-2))))
        return res