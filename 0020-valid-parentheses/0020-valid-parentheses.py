class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        check={")":"(","}":"{","]":"["}
        for i in s:
            if(i in check):
                if(len(stack)!=0 and check[i]==stack[-1]):
                    stack.pop()
                else:
                    return False

            else:
                stack.append(i)
        return len(stack)==0
    
   