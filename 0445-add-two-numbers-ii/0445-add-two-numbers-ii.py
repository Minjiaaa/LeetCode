# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #堆+循环
        st1 = []
        st2 = []
        while l1:
            st1.append(l1.val)
            l1 = l1.next
        
        while l2:
            st2.append(l2.val)
            l2 = l2.next
        
        carry = 0 #定义进位
        dummy = ListNode(0)
        
        while st1 or st2 or carry:
            adder1 = st1.pop() if st1 else 0
            adder2 = st2.pop() if st2 else 0
            sum_ = adder1 + adder2 + carry
            if sum_ >= 10:
                carry = 1
                sum_ -= 10
            else:
                carry = 0
            
            cur = ListNode(sum_)
            cur.next = dummy.next
            dummy.next = cur
        
        return dummy.next
        