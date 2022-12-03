# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            #if there is no elements to construct subtrees 
            #为什么这个限制条件写成这样？
                       
            val = postorder.pop()
            root = TreeNode(val)
            #the last element as the root
            index = idx_map[val] #root splits inorder list into left and right subtrees
            
            # build right subtree
            root.right = helper(index + 1, in_right)
            # build left subtree
            root.left = helper(in_left, index - 1)
            return root
        # build a hashmap value -> its index
        idx_map = {val:idx for idx, val in enumerate(inorder)} 
        return helper(0, len(inorder) - 1)
