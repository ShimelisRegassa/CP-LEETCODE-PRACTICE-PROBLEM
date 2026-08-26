class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        check={}
        stack=[]
        for i in nums2:
            while(stack and stack[-1]<i):
                temp=stack.pop()
                check[temp]=i
            stack.append(i)
        res=[-1]*len(nums1)
        for i in range(len(nums1)):
            if(nums1[i] in check):
                res[i]=check[nums1[i]]
        return res


