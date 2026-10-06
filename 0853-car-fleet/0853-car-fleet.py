class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        num=[]
        for i in range(len(position)):
            num.append((position[i],speed[i]))
        num.sort(key=lambda x:-x[0])
        counter=0
        t1=(target-num[0][0])/num[0][1]
        for i in range(1,len(num)): 
            t2=(target-num[i][0])/num[i][1]
            if(t2>t1):
                counter+=1
                t1=t2
            else:
                continue
        return counter+1
        