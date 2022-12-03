class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(i, nums, res)
        return res
    def twoSum(self, i, nums, res):
        lo = i + 1
        hi = len(nums) - 1
        while lo < hi:
            sum2 = nums[i] + nums[lo] + nums[hi]
            if sum2 < 0:
                lo += 1
            elif sum2 > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1 #去重