class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        for i in nums1:
            val=nums2.index(i)
            for j in range(val+1,len(nums2)):
                if(nums2[j]>i):
                    result.append(nums2[j])
                    break
            else:
                result.append(-1)
        return result


