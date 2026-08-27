class Solution:
    def simplifyPath(self, path: str) -> str:
        temp=path.split("/")
        stack=[]
        for i in temp:
            if(i=="." or i==""):
                continue
            elif(i==".."):
                if(stack):
                    stack.pop()
            else:
                stack.append(i)
                
        return "/" +"/".join(stack)
            

            
      

        