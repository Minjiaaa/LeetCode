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
#     # 要使用双指针,慢指针只有在满足条件的时候才会往前移动
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
        
        for j in range(index, len(nums)):
            nums[j] = 0
