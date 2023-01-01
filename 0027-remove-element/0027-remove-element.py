class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # slow = 0
        # fast = 0
        # while fast < len(nums):
        #     if nums[fast] != val:
        #         nums[slow] = nums[fast]
        #         slow += 1
        #     fast += 1
        # return slow
        left = 0
        right = len(nums) - 1
        while left <= right:
            # 找左边等于val的元素,说明需要替换，从左边开始新元素
            while left <= right and nums[left] != val:
                left += 1
            # 找右边不等于val的元素，说明需要换到前面
            while left <= right and nums[right] == val:
                right -= 1
            # 将右边不等于val的元素覆盖左边等于val的元素
            if left < right:
                nums[left] = nums[right]
                left += 1
                right -= 1
        return left