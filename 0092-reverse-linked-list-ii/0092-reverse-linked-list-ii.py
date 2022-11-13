# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = p = ListNode(None)
        dummy.next = head
        for i in range(left - 1):
            p = p.next #链表中的遍历。连着后面的一个tail
        tail = p.next
        
        for i in range(right - left): #这边需要自己画图总结出来交换的次数
            tmp = p.next
            p.next = tail.next
            tail.next = tail.next.next
            p.next.next = tmp #为什么不等于tail
        
        return dummy.next #dummy.next就表示新链表

            # 1-2-3-4-5
            # p-tail
            # 1-3-2-4-5
            # 2-4-3-2-5
            
            
