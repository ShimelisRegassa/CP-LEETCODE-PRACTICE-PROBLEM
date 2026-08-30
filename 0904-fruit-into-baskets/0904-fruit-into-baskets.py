class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        ob={}
        right=0
        long=0
        while(right<len(fruits)):
            ob[fruits[right]]=ob.get(fruits[right],0)+1
            while(left<right and len(ob)>2):
                ob[fruits[left]]-=1
                if(ob[fruits[left]]==0):
                    del ob[fruits[left]]
                left+=1
            long=max(long,right-left+1)

            right+=1
        return long



        