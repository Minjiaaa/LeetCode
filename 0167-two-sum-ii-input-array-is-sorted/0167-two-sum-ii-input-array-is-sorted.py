class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum2 = numbers[left] + numbers[right]
            if sum2 == target:
                return [left + 1, right + 1]
            elif sum2 < target:
                left += 1
            elif sum2 > target:
                right -= 1
        