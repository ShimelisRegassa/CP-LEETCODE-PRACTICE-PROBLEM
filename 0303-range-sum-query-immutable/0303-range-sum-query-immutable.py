class NumArray:

    def __init__(self, nums: List[int]):
        self.array=[]
        count=0
        for i in range (len(nums)):
            self.array.append(nums[i]+count)
            count+=nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        if(left==0):
            return self.array[right]
        return self.array[right]-self.array[left-1]
        

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)