# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        move = head
        
        while move.next is not None:
            if move.val == move.next.val:
                move.next = move.next.next
            else:#为什么这个else一定得写？
                move = move.next
        return head
