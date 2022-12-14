class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        allSum = 0
        preSum = 0
        for i in range(len(nums)):
            allSum += nums[i]
        
        for i in range(len(nums)):
            if preSum == allSum - preSum - nums[i]:
                return i
            preSum += nums[i]
        
        return -1