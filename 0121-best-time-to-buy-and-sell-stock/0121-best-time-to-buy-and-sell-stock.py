class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPro = float('inf')
        #maxPro = 0
        maxPro = 0
        for i in range(len(prices)):
            if prices[i] < minPro:
                minPro = prices[i]
            elif prices[i] - minPro > maxPro:
                maxPro = prices[i] - minPro
                #为什么是这么写的？
        return maxPro
            
            
            
            
            
            
            
            
        