class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('-inf')
        nums.sort()
        for i in range(len(nums)):
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                sum3 = nums[i] + nums[lo] + nums[hi]
                if abs(sum3 - target) < abs(diff):
                    diff = target - sum3
                if sum3 < target:
                    lo += 1
                else:
                    hi -= 1
                if diff == 0:
                    break
        return target - diff