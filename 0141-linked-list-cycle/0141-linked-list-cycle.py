# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
#hash table
        cnt = set()
        move = head
        while move is not None:
            if move in cnt:
                return True
            cnt.add(move)
            move = move.next
        return False
            
#two pointers
        # slow = fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         return True
        # return False
            
            
        