class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        res=[]
        ob={}
        for i in nums2:
            while(stack and stack[-1]<i):
                ob[stack[-1]]=i
                stack.pop()
            stack.append(i)
        for i in  nums1:
            if(i in ob):
                res.append(ob[i])
            else:
                res.append(-1)
        return res


