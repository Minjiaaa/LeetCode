class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        i = j = 0
        res = [ ]
        
        while j < len(nums):
            while j + 1 < len(nums) and nums[j] + 1 == nums[j + 1]:
                j += 1
            if i == j:
                res.append(str(nums[i]))
            else:
                res.append(f'{nums[i]}->{nums[j]}')
            i = j + 1
            j = i
        return res