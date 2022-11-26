# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
# 终止条件：当两个链表都为空时，表示我们对链表已合并完成。
# 如何递归：我们判断 l1 和 l2 头结点哪个更小，然后较小结点的 next 指针指向其余结点的合并结果。（调用递归）

        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        if list1.val <= list2.val:
            node = list1 #这一步是干嘛
            node.next = self.mergeTwoLists(list1.next, list2)
        else:
            node = list2
            node.next = self.mergeTwoLists(list1, list2.next)
        return node #为什么这里要返回？