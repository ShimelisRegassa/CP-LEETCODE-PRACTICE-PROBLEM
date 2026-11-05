# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if(not head or not head.next):
            return True
        fast=head
        slow=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        if fast:
            slow=slow.next
        prev=None
        current=slow
        while(current):
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        firs=head
        sec=prev
        while(sec):
            if(firs.val!=sec.val):
                return False
            firs=firs.next
            sec=sec.next
        return True
        
        
