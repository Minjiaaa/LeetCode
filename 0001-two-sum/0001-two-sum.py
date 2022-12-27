class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            hashMap[num] = i    
        for i in range(len(nums)):
            if target - nums[i] in hashMap and hashMap[target -  nums[i]] != i:
                return i, hashMap[target -  nums[i]]
        