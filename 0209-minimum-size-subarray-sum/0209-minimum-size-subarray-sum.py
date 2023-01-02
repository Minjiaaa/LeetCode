class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf") # 要求最小值，起始值赋一个最大值
        i = 0
        cur_sum = 0
        # 枚举法
        for j in range(len(nums)):
            cur_sum += nums[j]
            while cur_sum >= target:
                    res = min(res, j - i + 1)
                    cur_sum -= nums[i]
                    i += 1 # 往后找是否还有符合的元素
        return 0 if res == float("inf") else res
                    