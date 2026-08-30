# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(head is None or head.next is None):
            return False
        left=head
        right=head
        while(right is not None and right.next is not None):
            left=left.next
            right=right.next.next
            if(left==right):
                return True
        return False
        