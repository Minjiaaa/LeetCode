class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        curNums = []
        curSum = allSum = 0
        for i in range(n + 1):
            curNums.append(i)
        allSum = sum(curNums)
        for i in range(n):
            curSum += nums[i]
        return allSum - curSum
        

        