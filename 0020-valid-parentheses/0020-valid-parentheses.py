class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        check={")":"(","}":"{","]":"["}
        for i in s:
            if(i in check.values()):
                stack.append(i)
            elif(i in check.keys()):
                if(len(stack)==0 or check[i]!=stack[-1]):
                    return False
                stack.pop()
        return len(stack)==0
    
   