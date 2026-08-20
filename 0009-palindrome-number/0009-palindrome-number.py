class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        else:
            num1=str(x)
            if(num1==num1[::-1]):
                return True
            else:
                return False

        