class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        current=blocks[:k].count("W")
        res=current
        for i in range(k,len(blocks)):
            if(blocks[i]=="W"):
                current+=1
            if(blocks[i-k]=="W"):
                current-=1
            res=min(current,res)
        return res



        