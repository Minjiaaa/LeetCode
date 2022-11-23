class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        table = {0:1} 
        cnt = 0
        preSum = 0
        for i in range(len(nums)):
            preSum += nums[i]
            if preSum - k in table: 
                cnt += table[preSum - k]
            if preSum in table:
                table[preSum] += 1
            else:
                table[preSum] = 1

        return cnt
        #preSum[j] - preSum[i] == k
        # preSum = [0] * (len(nums) + 1)
        # for i in range(len(nums)):
        #     preSum[i + 1] = preSum[i] + nums[i]  

        #如何处理减法
        
        # #穷举法， 时间复杂度是O(n^2), tle，
        # cnt = 0
        # for i in range(len(nums)):
        #     preSum = 0
        #     for j in range(i, len(nums)):
        #         preSum += nums[j]
        #         if preSum == k:
        #             cnt += 1
        # return cnt

        

                
        