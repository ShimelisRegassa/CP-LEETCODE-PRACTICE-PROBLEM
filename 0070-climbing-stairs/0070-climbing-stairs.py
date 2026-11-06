class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        def stairclimb(n):
            if(n==1):
                return 1
            if(n==2):
                return 2
            if n in memo:
                return memo[n]
            memo[n]=stairclimb(n-1)+stairclimb(n-2)
            return memo[n]
        return stairclimb(n)
        