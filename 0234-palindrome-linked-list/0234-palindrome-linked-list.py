# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        cur = slow.next
        
        while cur:
            nodeNext = cur.next
            cur.next = prev
            prev = cur
            cur = nodeNext
        
        while prev:
            if prev.val != head.val:
                return False
            prev, head = prev.next, head.next
            
        return True