# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #stack+iteration
        if root is None:
            return []
        
        res = []
        stack = [root, ]
        
        while stack:
            root = stack.pop()
            if root is not None:
                res.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        return res
                
            
# 超出时间限制
#         if not root: # root is None:
#             return []
        
#         res = []
#         stack = []
#         curr = root
        
#         while curr or stack:
#             if not curr:
#                 curr = stack.pop()
#             while curr:
#                 res.append(curr.val)
#             if curr.right:
#                 res.append(curr.right)
#             curr = curr.left
#         return res
            
        
        