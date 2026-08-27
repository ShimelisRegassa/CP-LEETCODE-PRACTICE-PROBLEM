class Solution:
    def simplifyPath(self, path: str) -> str:
        temp=path.split("/")
        stack=[]
        for i in temp:
            if(i=="." or i==""):
                continue
            elif(stack and i==".."):
                stack.pop()
            elif(i!="//" or i!="///"):
                if(i!=".."):
                    stack.append(i)
        return "/" +"/".join(stack)
            

            
      

        