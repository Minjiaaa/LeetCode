"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
#         if not root:
#             return []
#         for child in root.children:
#             self.postorder(child)
#         self.res.append(root.val)
#         return self.res
        
#         stack = [root]
#         [3, 2, 4]
        
#         stack = [5, 6]
        
        
#         ans = [1, 4, 2, 3]
        if not root:
            return []
        res = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children)
        return res[::-1]