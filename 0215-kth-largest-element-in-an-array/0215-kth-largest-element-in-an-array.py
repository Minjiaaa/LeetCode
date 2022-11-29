class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #bruteforce
        n = len(nums)
        nums.sort()
        return nums[n-k]
        