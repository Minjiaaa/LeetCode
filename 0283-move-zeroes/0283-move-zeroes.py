class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
#         if len(nums) == 0:
#             return nums
        
#         else:
#             for i in range(len(nums) - 1):
#                 while nums[i] == 0:
#                     nums[i], nums[i+1] = nums[i+1], nums[i]
#         #             i += 1
#         # i = 0, nums[0], nums[1] = nums[1], nums[0] 1, 0, 0, 3, 12
#         #                                             1, 0, 0, 3, 12
#         #                                              1, 0, 3, 0, 12   
#     # 要使用双指针
        i = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
