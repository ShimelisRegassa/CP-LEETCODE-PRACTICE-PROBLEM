class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        res=[]
        nums.sort()
        prefix=[0]*len(nums)
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            prefix[i]=total
        for j in  queries:
            for i in range(len(prefix)):
                if(j>=prefix[i]):
                    if(i==len(prefix)-1):
                        res.append(i+1)
                        break
                    else:
                        continue
                  
                else:
                    res.append(i)
                    break
        return res
        


        

        