# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        right=list1
        left=list2
        current=dummy
        while(right and left):
            if(right.val>left.val):
                current.next=left
                left=left.next
            else:
                current.next=right
                right=right.next
            current=current.next
        if(right):
            current.next=right
        if(left):
            current.next=left
        return dummy.next


        
   

            

    
        
        