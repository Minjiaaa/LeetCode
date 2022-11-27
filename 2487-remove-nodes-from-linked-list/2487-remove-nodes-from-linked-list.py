# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(pre):
            cur = pre.next
            if not cur.next:
                return cur.val
            curMax = dfs(cur)
            if curMax > cur.val:
                pre.next = cur.next
            return max(curMax, cur.val)
        dummy = ListNode(0)
        dummy.next = head
        dfs(dummy)
        return dummy.next
    # def reverse(self, head):
    #     tail = None
    #     while head:
    #         nextNode = head.next
    #         head.next = tail
    #         tail = head
    #         head = nextNode
    #     return tail
    # def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     curr = tail = self.reverse(head)
    #     maxNode = curr
    #     while curr is not None and curr.next is not None:
    #         if curr.next.val < maxNode.val:
    #             curr.next = curr.next.next
    #         else:
    #             curr = curr.next
    #             maxNode = curr
    #     return self.reverse(tail)
    #有recursion和dfs的思路，但是不知道如何下手，感觉可以分成小问题，但是不知道如何进一步解决
    #   while head is not None:
    #   head = head.next
        # find the target node and delete the node
            
        