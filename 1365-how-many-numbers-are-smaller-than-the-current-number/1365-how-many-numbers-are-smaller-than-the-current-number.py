class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num= 0
        result =[]
        while(num<len(nums)):
            count=0
            for i in range (len(nums)):
            
                if(nums[num]>nums[i]):
                    count +=1
            num+=1
            result.append(count)
        return result

        