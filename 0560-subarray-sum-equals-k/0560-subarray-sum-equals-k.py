class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ob={0:1}
        val=0
        counter=0
        for i in nums:
            val+=i
            if(val-k in ob):
                counter+=ob[val-k]
            ob[val]=ob.get(val,0)+1
        return counter

      