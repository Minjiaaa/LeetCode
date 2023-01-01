class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j, k = 0, n - 1, n - 1
        res = [-1] * n
        while i <= j:
            l2 = nums[i] ** 2
            r2 = nums[j] ** 2
            if l2 <= r2:
                res[k] = r2
                j -= 1
            else:
                res[k] = l2
                i += 1
            k -= 1
        return res
            