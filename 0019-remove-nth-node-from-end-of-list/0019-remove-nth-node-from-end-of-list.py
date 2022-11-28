# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = cur = dummy
        
        if head is None or head.next is None:
            return None
        #考虑n，题目限制条件
        for i in range(n+1):
            cur = cur.next
        while cur:
            cur = cur.next
            prev = prev.next
        
        prev.next = prev.next.next
        return dummy.next
            
            
        
        