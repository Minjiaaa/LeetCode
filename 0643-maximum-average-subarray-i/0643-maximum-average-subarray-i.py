class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSum = sum(nums[:k])
        maxSum = curSum
        for i in range(len(nums) - k):
            curSum -= nums[i]
            curSum += nums[i+k]
            maxSum = max(maxSum, curSum)
        return maxSum / k