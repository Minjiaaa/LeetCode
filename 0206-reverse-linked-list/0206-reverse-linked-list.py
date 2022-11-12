# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recur(cur, pre):
            #Base Case and also the terminated condition
            if not cur: #当cur为空
                return pre
            res = recur(cur.next, cur) #记录反转列表的头节点
            # recursion
            cur.next = pre #修改当前节点指向前面的节点，一直逼近base case
            return res
        return recur(head, None) 
        