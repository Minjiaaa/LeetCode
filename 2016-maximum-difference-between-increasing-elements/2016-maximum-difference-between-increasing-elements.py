class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min = float('inf')
        max = 0
        for i in range(len(nums)):
            if nums[i] < min:
                min = nums[i]
            elif nums[i] - min > max:
                max = nums[i] - min
        if max == 0:
            return -1
        else:
            return max