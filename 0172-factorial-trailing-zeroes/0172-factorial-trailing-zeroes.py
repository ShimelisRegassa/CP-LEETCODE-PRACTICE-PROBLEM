import sys
sys.set_int_max_str_digits(0)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if(n==0 or n==1):
            return 0
        def recursion(m):
            if(m==1):
                return 1
            return m*recursion(m-1)
        v=recursion(n)
        v=str(v)
        counter=0
        for i in range(len(v)-1,-1,-1):
            if(v[i]=="0"):
                counter+=1
            else:
                break
        return counter