class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        counter=0
        for i in s:
            if(i=="("):
                stack.append(0)
            else:
                inner=stack.pop()
                score=0
                if(inner==0):
                    score=1
                else:
                    score=2*inner
                stack[-1]+=score
        return stack[-1]
                    


               


    