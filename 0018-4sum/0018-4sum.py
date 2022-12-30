class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                total = target - nums[i] - nums[j]
                left, right = j + 1, len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == total:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > total:
                        right -= 1
                    else:
                        left += 1
        return result
#         nums.sort()
#         if len(nums) < 4:
#             return []
#         res = []
#         for i in range(len(nums) - 3):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             for j in range(i + 1, len(nums) - 2):
#                 if j > i + 1 and nums[j] == nums[j - 1]:
#                     continue
#                 self.twoSum(j, nums, res, target - nums[j])
                    
    
#     def twoSum(self, k, nums, res, target):
#         lo = k + 1
#         hi = len(nums) - 1
#         while lo < hi:
#             cur_sum = nums[lo] + nums[hi]
#             if cur_sum < target:
#                 lo += 1
#             elif cur_sum > target:
#                 hi += 1
#             else:
#                 res.append([nums[lo], nums[hi]])
#                 lo += 1
#                 hi -= 1
#         return res
            