class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out=[]
        l1=set(nums1)
        l2=set(nums2)
        res=l1 & l2
        for i in res:
            a=min(nums1.count(i),nums2.count(i))
            for j in range(a):
                out.append(i)
        return out
        

        