class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        j = 1
        for i in range(len(nums)):
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            if j >= len(nums):
                break
            nums[i + 1] = nums[j]
            
        return i + 1