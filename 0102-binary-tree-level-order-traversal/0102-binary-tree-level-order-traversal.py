# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
#         res = []
        
#         # deque是双端队列，相当于是给deque传入了一个值为root的list
#         queue = deque([root])
        
#         while queue:
#             res.append([node.val for node in queue])
            
#             for i in range(len(queue)):
#                 node = queue.popleft()
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
                    
#         return res
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []

#         queue = [root]
#         res = []

#         while queue:
#             next_queue = []
#             res.append([node.val for node in queue])
#             for node in queue:
#                 if node.left:
#                     next_queue.append(node.left)
#                 if node.right:
#                     next_queue.append(node.right)
#             queue = next_queue
#         return res
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root, None])
        res = []
        level = []
        while queue:
            node = queue.popleft()
            if node is None:
                res.append(level)
                level = []
                if queue: #这里是啥意思？
                    queue.append(None)
                continue
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res