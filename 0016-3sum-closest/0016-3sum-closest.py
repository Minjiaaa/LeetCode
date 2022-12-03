class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                complement = target - nums[i] - nums[j]
                hi = bisect_right(nums, complement, j + 1)
                lo = hi - 1
                if hi < len(nums) and abs(complement - nums[hi]) < abs(diff):
                    diff = complement - nums[hi]
                if lo > j and abs(complement - nums[lo]) < abs(diff): #
                    diff = complement - nums[lo]
            if diff == 0:
                break
        return target - diff
                
        # Two Pointers
        #     lo = i + 1
        #     hi = len(nums) - 1
        #     while lo < hi:
        #         sum3 = nums[i] + nums[lo] + nums[hi]
        #         if abs(sum3 - target) < abs(diff):
        #             diff = target - sum3
        #         if sum3 < target:
        #             lo += 1
        #         else:
        #             hi -= 1
        #         if diff == 0:
        #             break
        # return target - diff