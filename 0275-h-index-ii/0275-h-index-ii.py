class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n=len(citations)
        right=n-1
        left=0
        while(left<=right):
            mid=left+(right-left)//2
            h=n-mid
            if(citations[mid]>h):
                right=mid-1
            elif(citations[mid]<h):
                left=mid+1
            else:
                return h
        return n-left
                