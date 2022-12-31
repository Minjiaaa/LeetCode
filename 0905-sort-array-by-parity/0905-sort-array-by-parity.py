class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            if nums[left] % 2 > nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]
            while left <= right and nums[left] % 2 == 0:
                left += 1
            while left <= right and nums[right] % 2 == 1:
                right -= 1

                
        return nums
        
        
        