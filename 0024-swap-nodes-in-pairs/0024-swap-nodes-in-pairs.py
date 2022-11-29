# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        prev = dummy
        cur = head
        while cur and cur.next:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = cur
            prev.next = tmp
            
            prev = cur
            cur = cur.next
            #这里不理解
        return dummy.next
            
        