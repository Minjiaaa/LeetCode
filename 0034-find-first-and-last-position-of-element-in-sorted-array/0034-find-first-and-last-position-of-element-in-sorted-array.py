class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]
    def binSearch(self, nums, target, isFirst):
        l, r = 0, len(nums) - 1

        while l <= r: # We iterate until begin is greater than to end.
            m = (r  - l) // 2 + l
            if nums[m] == target:
                if isFirst:
                    # find the lower bound
                    if m == l or nums[m - 1] < target:  #[3, 6, 7]
                        return m
                    r = m - 1 #寻找左边界，就要在nums[middle] == target的时候更新right(如果有很多个重复的数字，可以一直减)
                else:
                    # found the right bound
                    if m == r or nums[m + 1] > target:
                        return m
                    l = m + 1 # 当nums[middle] == target的时候，更新left，这样才能得到target的右边界
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
                
        return -1
"""neetcode的方法太强了，就是这里没明白"""
