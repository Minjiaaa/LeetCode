class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        stack = []
        for num in nums2:
            stack.append(num)
        
        for num in nums1:        
            temp = []
            isFound = False
            nextMax = -1
            while len(stack) != 0 and not isFound:
                top = stack.pop()
                if top > num:
                    nextMax = top
                elif top == num:
                    isFound = True
                temp.append(top)
            res.append(nextMax)
            while len(temp) != 0:
                stack.append(temp.pop())
        return res
        
        
            
        
        