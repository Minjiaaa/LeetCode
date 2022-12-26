class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (r -l) // 2 + l
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l
        #不知道应该怎么找到那个数
                    