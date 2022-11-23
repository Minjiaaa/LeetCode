class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left + (right - left) // 2] < target:
                left += 1
            elif nums[left + (right - left) // 2] > target:
                right -= 1
            else:
                return left + (right - left) // 2
        return -1
        