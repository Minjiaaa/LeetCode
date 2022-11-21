class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #1.定义需要维护的变量
        maxAvg = float('-inf')
        curSum = 0
        #2. 定义窗口的首尾端
        left = 0
        for right in range(len(nums)):
            
            #3. 更新需要维护的变量
            curSum += nums[right]
            if right - left + 1 == k:
                maxAvg = max(curSum / k, maxAvg)
           
            #4 if窗口长度达到限定，1）更新维护变量，2）窗口移动
            if right >= k - 1:
                curSum -= nums[left]
                left += 1 #这一步确保了以固定窗口移动     
        return maxAvg
        
        
            # while right - left + 1 == k:
            #     maxAvg = max(sum(nums[left:right + 1])/4, maxAvg)
            #为什么这么写会tle
            # if right - left + 1 == k:
        # [1, 12, -5, -6, 50, 3]
        # left = 0, right = 3, maxAvg = 0.5
        # right = 4, left = 1, maxavg = 12.75
        # right = 5, left = 2, maxAvg = (12.75, 10.5)
        