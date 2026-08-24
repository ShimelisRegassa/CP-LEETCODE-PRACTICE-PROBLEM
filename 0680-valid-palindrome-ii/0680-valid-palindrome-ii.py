class Solution:
    def validPalindrome(self, s: str) -> bool:
        right=len(s)-1
        left=0
        k=2
        b=0
        c=0
        while(left<=right):
            if(s[left]==s[right]):
                right-=1
                left+=1
            else:
                if(k==2):
            
                    b=right
                    c=left
                    left+=1
                    k-=1
                elif(k==1):
                    right=b
                    left=c
                    right-=1
                    k-=1
                else:
                    return False
        return True
              
            

        