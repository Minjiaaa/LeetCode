class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        
        preFix = [1] * (n + 1)
        for i in range(n):
            preFix[i + 1] = preFix[i] * nums[i]
        

        postFix = [1] * (n + 1)
        for i in range(n - 1, -1, -1):
            postFix[i] = postFix[i + 1] * nums[i]
            
        
        for i in range(n):
            res.append(preFix[i] * postFix[i + 1])
        
        return res