class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def mergesort(nums):
            if(len(nums)<=1):
                return nums
            mid=len(nums)//2
            left=mergesort(nums[:mid])
            right=mergesort(nums[mid:])
            result=[]
            i,j=0,0
            while(len(left)>i and len(right)>j):
                if(left[i]<right[j]):
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        return mergesort(nums)
        
                
                


            

