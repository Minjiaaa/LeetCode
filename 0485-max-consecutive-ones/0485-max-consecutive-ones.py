class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        if len(nums) == 0:
            return 0
        
        else:
            for i in range(len(nums)):
                if nums[i] == 1:
                    count += 1
                    res = max(count, res)
                else:
                    count = 0 
        return max(count, res)