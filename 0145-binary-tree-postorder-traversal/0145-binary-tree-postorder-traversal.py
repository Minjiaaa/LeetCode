# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        stack = [[root, 0]] #
        res = []
        
        while stack:
            top = stack[-1]
        
            if top[1]:
                stack.pop()
                if top[0].left:
                    stack.append([top[0].left, 0])
            else:
                res.append(top[0].val)
                top[1] = 1

                if top[0].right:
                    stack.append([top[0].right, 0])
        
        return res[::-1]