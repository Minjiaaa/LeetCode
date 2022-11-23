class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        table = {0:1} 
        cnt = 0
        preSum = 0
        for i in range(len(nums)):
            preSum += nums[i]
            target = preSum - k   #目标前缀和：使得 当前前缀和-目标前缀和=k
            
            if target in table:   #查看是否有我们的目标前缀和，如果有，将他出现的次数加入到count
                cnt += table[target]
            #避免k = 0的情况
            table[preSum] = table.get(preSum, 0) + 1  #更新当前前缀和出现的次数
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

        

                
        