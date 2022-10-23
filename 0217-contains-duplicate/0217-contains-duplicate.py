class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
#         cnt = {}
        
#         for num in nums:
#             cnt[num] = cnt.get(num, 0) + 1
            
#             if cnt[num] > 1:
#                 return True
        return len(nums) > len(set(nums))
        #如何保证每一个和任何一个？
        #用set计数

        cnt = {}
        
        for num in nums:
            if num not in cnt:
                cnt[num] += 1
            else:
                return True
        return False
                
                
                
        
        