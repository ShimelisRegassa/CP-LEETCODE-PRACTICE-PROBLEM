class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n=len(num)
        counter=""
        for i in range(n-2):
            temp=num[i:i+3]
            if(len(set(temp))==1):
                if(counter==""):
                    counter=temp
                elif(int(counter[0])<int(temp[0])):
                    counter=temp
                
        return counter



        