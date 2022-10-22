class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = {}
        
        for s in nums:
            cnt[s] = cnt.get(s, 0) + 1
            if cnt[s] > len(nums) // 2:
                return s
                