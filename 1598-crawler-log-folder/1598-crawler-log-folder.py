class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for i in logs:
            if(i=="../" and stack):
                stack.pop()
            elif(i=="./"):
                continue
            elif(i!="../" and i!="./" and i!="x/"):
                stack.append(i)
            else:
                continue
        return len(stack)


        