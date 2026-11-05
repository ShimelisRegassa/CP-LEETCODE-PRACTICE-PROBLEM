# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        res=[]
        current=head
        while(current):
            res.append(current.val)
            current=current.next
        right=len(res)-1
        left=0
        while(left<right):
            if(res[right]==res[left]):
                left+=1
                right-=1
            else:
                return False
        return True
        
