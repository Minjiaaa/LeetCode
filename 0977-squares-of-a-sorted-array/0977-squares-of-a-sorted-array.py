class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j, k = 0, n - 1, n - 1
        res = [-1] * n
        while i <= j:
            lm = nums[i] ** 2
            rm = nums[j] ** 2
            if lm > rm:
                res[k] = lm
                i += 1
            else:
                res[k] = rm
                j -= 1
            k -= 1
        
        return res
        