class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashMap = {}
        # for i, num in enumerate(nums):
        #     hashMap[num] = i    
        # for i in range(len(nums)):
        #     if target - nums[i] in hashMap and hashMap[target -  nums[i]] != i:
        #         return i, hashMap[target -  nums[i]]
        nums_ = [
        (num, index) for index, num in enumerate(nums)
    ]
        nums_.sort()

        # tuple的排序先根据第一个数字，再根据第二个数字
        #print(nums_)
        left, right = 0, len(nums_) - 1
        while left < right:
            if nums_[left][0] + nums_[right][0] > target:
                right -= 1
            elif nums_[left][0] + nums_[right][0] < target:
                left += 1
            else:
                return sorted([nums_[left][1], nums_[right][1]])