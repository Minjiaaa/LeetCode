# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
# 终止条件：当两个链表都为空时，表示我们对链表已合并完成。
# 如何递归：我们判断 l1 和 l2 头结点哪个更小，然后较小结点的 next 指针指向其余结点的合并结果。（调用递归）

        if not list2: return list1
        if not list1: return list2
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1 #为什么这里要返回？
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2 #为什么这里要返回？