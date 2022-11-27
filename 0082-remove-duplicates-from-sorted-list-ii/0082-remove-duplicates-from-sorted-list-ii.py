# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        move = dummy
        if head is None:
            return None
        while move.next is not None and move.next.next is not None:
            if move.next.val == move.next.next.val:
                movePre = move.next.val
                while move.next is not None and move.next.val == movePre:
                    move.next = move.next.next
            else:
                move = move.next
        return dummy.next
            
        