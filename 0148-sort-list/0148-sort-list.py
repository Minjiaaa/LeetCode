# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         slow = slow.next
#         fast = 0
#         #如何使用快慢指针找到链表中点 
#         #如何定义右指针
        if not head or not head.next:
            return head
        slow = head
        fast = head
        #用快慢指针分成两部分
        while fast.next and fast.next.next:#这里的终止条件怎么判定的？
            slow = slow.next
            fast = fast.next.next
        
        #找到左右两部分，把左边部分置空
        mid = slow.next
        slow.next = None
        
        #开始递归
        left = self.sortList(head)
        right = self.sortList(mid)
        
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        move = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                move.next = l1
                l1 = l1.next
            else:
                move.next = l2
                l2 = l2.next
            move = move.next
        move.next = l1 if l1 else l2
        return dummy.next
                
#用两次recursion会超时  
#     def merge(self, l1, l2):
#         if not l1:
#             return l2
#         elif not l2:
#             return l1
        
#         if l1.val < l2.val:
#             node = l1
#             node.next = self.merge(l1.next, l2)
#         else:
#             node = l2
#             node.next = self.merge(l1, l2.next)
#         return node