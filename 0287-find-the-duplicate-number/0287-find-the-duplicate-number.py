class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cnt = {}
        for i in range(len(nums)):
            cnt[nums[i]] = cnt.get(nums[i], 0) + 1
        for v in cnt:
            if cnt[v] > 1:
                return v
        # left = 0, right = len(nums) - 1
        # while left < right:
        #     if nums[left] != 
        
        