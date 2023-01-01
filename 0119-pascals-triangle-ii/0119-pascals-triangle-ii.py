class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        nums = [1]
        for i in range(1, rowIndex + 1):
            nums.insert(0, 0)
            for j in range(i):
                nums[j] = nums[j] + nums[j + 1]
        return nums
        