class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 将两个指针先指向数组的头部
        slow, fast = 0, 0
        while fast < len(nums):
            # 遇到非0数复制给新数组指针指向的位置
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                # 将left往后移动一位
                slow += 1
            fast += 1
        
        while slow < len(nums):
            nums[slow] = 0
            slow += 1
        