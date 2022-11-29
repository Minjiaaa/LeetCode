# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        hasCycle = False
        while not hasCycle and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            hasCycle = slow == fast
        if not hasCycle:
            return None
        
        p = head
        while p != slow:
            p = p.next
            slow = slow.next
        
        return p
        #p就是链表的指针啊