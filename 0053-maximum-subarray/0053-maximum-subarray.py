class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.getMax(nums, 0 , len(nums) - 1)
    
    def getMax(self, nums, left, right):
        if left == right:
            return nums[left]

        mid = left + (right - left) // 2

        leftMax = self.getMax(nums, left, mid)
        rightMax = self.getMax(nums, mid + 1, right)
        crossMax = self.CrossMax(nums, left, right)

        return max(leftMax, rightMax, crossMax)

    def CrossMax(self, nums, left, right):
        mid = left + (right - left) // 2 #取整数
        leftSum = nums[mid] #这一点没明白
        leftMax = leftSum
        for i in range(mid - 1, left - 1, -1): #中间，递减，直到左边
            leftSum = leftSum + nums[i]
            leftMax = max(leftSum, leftMax)

        rightSum = nums[mid + 1]
        rightMax = rightSum
        for i in range(mid + 2, right + 1):
            rightSum = rightSum + nums[i]
            rightMax = max(rightSum, rightMax)
        return leftMax + rightMax