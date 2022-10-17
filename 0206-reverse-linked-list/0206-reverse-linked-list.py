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
            #先分别设定两个节点，然后不要动原来的链表，先设定头指针，注意有些节点断开之后没有指针了。
            dummy.next = hnext
            head.next = hnext.next #需要使用head这个指针
            hnext.next = dnext
           
        return dummy.next
            
        