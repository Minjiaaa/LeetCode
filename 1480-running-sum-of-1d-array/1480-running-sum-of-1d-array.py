class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            res[i] += res[i - 1] + nums[i]
        return res[:len(nums)]