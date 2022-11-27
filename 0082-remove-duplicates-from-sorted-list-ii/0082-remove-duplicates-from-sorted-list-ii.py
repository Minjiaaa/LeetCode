# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        move = head
        
        #move.next
        while move is not None and move.next is not None:
            #no duplicates
            if move.next and move.next.val != move.val:
                prev = prev.next
                move = move.next
                continue
            
            #duplicates exist
            while move.next and move.next.val == move.val:
                move.next = move.next.next
            move = move.next
              
            #remove the first duplicate
            prev.next = prev.next.next
            
        return dummy.next

        