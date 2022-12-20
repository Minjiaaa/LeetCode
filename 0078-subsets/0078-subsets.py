class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        
        def helper(nums, index):
            # 收集子集，要先于终止判断，否则会漏掉自己
            res.append(path[:])
            
            # Base
            if index == len(nums):
                
                return
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                helper(nums, i + 1)
                path.pop()
        
        helper(nums, 0)
        return res
            
            