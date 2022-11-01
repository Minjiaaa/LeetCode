class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxCount = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
                maxCount = max(count, maxCount)
            else:
                count = 1
        return maxCount
        