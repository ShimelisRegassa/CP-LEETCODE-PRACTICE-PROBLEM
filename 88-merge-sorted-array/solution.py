class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left1=0
        left2=0
        result=[]

        while(left1<=m-1 and left2<=n-1):

            if(nums1[left1]<=nums2[left2]):
                result.append(nums1[left1])
                left1+=1
            else:
                result.append(nums2[left2])
                left2+=1
        while(left1<m):
            result.append(nums1[left1])
            left1+=1
        while (left2<n):
            result.append(nums2[left2])
            left2 +=1
        nums1[:]=result

        