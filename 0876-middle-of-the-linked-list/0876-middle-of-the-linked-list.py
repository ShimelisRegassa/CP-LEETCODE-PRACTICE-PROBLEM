# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head.next is None):
            return head
        right=head
        left=head
        while((right is not None and right.next is not None) ):
            right=right.next.next
            left=left.next
        return left