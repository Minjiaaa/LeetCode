class Solution:
    def maxArea(self, height: List[int]) -> int: 
        l = 0
        r = len(height) - 1
        maxSum = 0
        
        while l < r:
            maxSum = max(maxSum, min(height[l], height[r]) * (r-l))
            if height[l] < height[r]:
                 l += 1
            else:
                r -= 1
            
        return maxSum
#         maxSum = 0
        
#         for l in range(len(height)):
#             for r in range(l+1, len(height)):
#                 width = r - l
#                 maxSum = max(maxSum, min(height[l], height[r]) * width)  
#         return maxSum
    