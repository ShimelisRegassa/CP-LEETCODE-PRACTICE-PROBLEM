class Solution:
    def isHappy(self, n: int) -> bool:
        b=str(n)
        while(len(b)>1):
            total=0
            for i in b:
                total+=(int(i)*int(i))
                b=str(total)
        n=int(b)
        if(n==1 or n==7):
            return True
        else:
            return False

        