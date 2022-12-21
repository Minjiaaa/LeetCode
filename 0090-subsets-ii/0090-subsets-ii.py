class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort()
        
        def helper(nums, index):
            
            res.append(path[:])
            if index == len(nums):
                return
            
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                helper(nums, i + 1)
                path.pop()
            
        helper(nums, 0)
        return res
        