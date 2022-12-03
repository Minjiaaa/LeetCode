class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i, x in enumerate(nums):
            arr.append([x, i])
        arr.sort()
        
        left = 0
        right = len(arr) - 1
        while left < right:
            sum2 = arr[left][0] + arr[right][0]
            if sum2 == target:
                return [arr[left][1], arr[right][1]]
            elif sum2 < target:
                left += 1
            elif sum2 > target:
                right -= 1

        
        