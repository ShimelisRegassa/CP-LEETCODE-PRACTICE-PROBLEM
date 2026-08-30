class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        for i in s:
            if i=="#" and stack1:
                stack1.pop()
            elif i=="#" and not stack1:
                continue
            else:
                stack1.append(i)
        for i in t:
            if i=="#" and stack2:
                stack2.pop()
            elif(i=="#" and not stack2):
                continue
            else:
                stack2.append(i)
        return stack1==stack2
        
        