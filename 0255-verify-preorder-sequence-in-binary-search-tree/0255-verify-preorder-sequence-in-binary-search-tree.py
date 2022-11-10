class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        new_min = float('-inf') #初始下限值
        for i in range(len(preorder)):
            if preorder[i] < new_min:
                return False
            while stack and preorder[i] > stack[-1]:
                new_min = stack.pop()
            stack.append(preorder[i])
        return True