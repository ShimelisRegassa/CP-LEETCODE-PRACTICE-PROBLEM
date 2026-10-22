# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        def mergesort(head):
            if not head or  not head.next:
                return head
            slow=head
            fast=head
            prev=None
            while(fast and fast.next ):
                prev=slow
                slow=slow.next
                fast=fast.next.next
            prev.next=None
            left=mergesort(head)
            right=mergesort(slow)
            dummy=ListNode(0)
            first=dummy
            while(left and right):
                if(left.val>right.val):
                    first.next=right
                    right=right.next
                else:
                    first.next=left
                    left=left.next
                first=first.next
            if(left):
                first.next=left
            if(right):
                first.next=right
            return dummy.next
        return mergesort(head)
                
          
            







            
        