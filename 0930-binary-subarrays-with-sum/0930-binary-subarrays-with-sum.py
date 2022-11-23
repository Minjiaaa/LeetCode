class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        preSum = 0
        table = {0 : 1}
        cnt = 0
        for i in range(len(nums)):
            preSum += nums[i]
            if preSum - goal in table:
                cnt += table[preSum - goal]
            table[preSum] = table.get(preSum, 0) + 1
        
        return cnt
            