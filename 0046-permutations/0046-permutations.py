class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    #dfs
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            #backtracking
        for i in range(len(nums)):
            self.dfs(nums[: i]+ nums[i + 1:], path + [nums[i]], res) #没看懂
            
