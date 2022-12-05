class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = -1
        left = 0
        right = len(nums) - 1
        while left < right:
            sum2 = nums[left] + nums[right]
            if sum2 < k:
                answer = max(answer, sum2)
                left += 1
            else:
                right -= 1
        return answer