class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = res = 0
        for num in nums:
            if count == 0:
                res = num
            
            if num != res:
                count -= 1
            else:
                count += 1
        return res

#HashMap
        
#         cnt = {}
        
#         for s in nums:
#             cnt[s] = cnt.get(s, 0) + 1
#             if cnt[s] > len(nums) // 2:
#                 return s
                