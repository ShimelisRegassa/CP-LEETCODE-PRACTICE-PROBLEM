class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        op="+/*-"
        for i in tokens:
            if(i in op):
                val1=(stack.pop())
                val2=(stack.pop())
                if(i=="+"):
                    stack.append(val1+val2)
                elif(i=="-"):
                    stack.append(val2-val1)
                elif(i=="*"):
                    stack.append(val1*val2)
                else:
                    temp=val2/val1
                    stack.append(int(temp))
            else:
                stack.append(int(i))
        return stack[0]


            
        
        