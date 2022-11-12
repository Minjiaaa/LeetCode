# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getPath(self, root, path, res):
        if not root:
            return
        #当前节点是root，path用来记录当前的路径，将某一个node加入path，path加入res用来添加结果
        path += str(root.val)
        if root.left == None and root.right == None:
            res.append(path)
        else:
            path += '->' #注意输出形式
            self.getPath(root.left, path, res)
            self.getPath(root.right, path, res)
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self.getPath(root, '', res)
        
        return res
        
        
        