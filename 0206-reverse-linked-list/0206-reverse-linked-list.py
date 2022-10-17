# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        while head != None and head.next != None:
            hnext = head.next
            dnext = dummy.next
            dummy.next = hnext
            head.next = hnext.next
            hnext.next = dnext
           
        return dummy.next
            
        