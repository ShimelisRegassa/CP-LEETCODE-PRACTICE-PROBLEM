class Solution:
    def interpret(self, command: str) -> str:
        count={"G":"G","()":"o","(al)":"al"}
        res=""
        left=0
        while(left<len(command)):
            if(command[left]=="(" and command[left+1]==")"):
                res+=(count["()"])
                left+=2
            elif(command[left]=="(" and command[left+1].isalpha()):
                res+=(count["(al)"])
                left+=4
            else:
                res+=(count["G"])
                left+=1
        return res



        