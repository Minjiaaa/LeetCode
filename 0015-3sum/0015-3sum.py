class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]: #[-1, -1, 2]
                continue
            self.twoSum(nums, i, res)
        return res
        
    def twoSum(self, nums, i, res):
        slow = i + 1
        fast = len(nums) - 1
        while slow < fast:
            cur_sum = nums[slow] + nums[fast] + nums[i]
            if cur_sum < 0:
                slow += 1
            elif cur_sum > 0:
                fast -= 1
            else:
                res.append([nums[i], nums[slow], nums[fast]])
                #print(res)
                slow += 1
                fast -= 1
                while slow < fast and nums[slow] == nums[slow - 1]:  #[0,0,0]
                    slow += 1