# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        h1 = l1 = ListNode(0, head)
        h2 = l2 = ListNode(0, head)
        move = head
        while move:
            if move.val < x:
                l1.next = move
                l1 = l1.next
            else:
                l2.next = move
                l2 = l2.next
            move = move.next
        l2.next = None
        l1.next = h2.next
        return h1.next
        