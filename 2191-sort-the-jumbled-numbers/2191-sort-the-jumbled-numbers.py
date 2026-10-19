class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        res={}
        check={}
        for i in range(len(nums)):
            total=""
            for j in str(nums[i]):
                total+=str(mapping[int(j)])
            res[i]=int(total)
            check[int(total)]=nums[i]
        fin=sorted(res.items(),key=lambda x:(x[1],x[0]))
        out=[]
        for x,y in fin :
            val=nums[x]
            out.append(val)
        return out
       

       
            
        


        