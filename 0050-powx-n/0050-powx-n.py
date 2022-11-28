class Solution:
    def myPow(self, x: float, n: int) -> float:
#         res = 1
        
            
#         for i in range(abs(n)):
#             res *= x
#         if n < 0:
#             res = 1 / res
#         return res
        
        
        
        
# 2000

# 1000

# 500
            
        
        memo = {}
# #         memo[0] = x^0
# #         memo[1] = x^1
# #             .....        
    
        negtive = True if n < 0 else False
        def dfs(n):
            nonlocal x
            if n == 0:
                return 1
            if n == 1:
                return x
            if n in memo:
                return memo[n]
            curRes = -1
            if n % 2 == 0:
                curRes = dfs(n // 2) * dfs(n // 2)
            else:
                curRes = dfs(n // 2) * dfs(n // 2) * x
            memo[n] = curRes
            return curRes
        tmp = dfs(abs(n))
        if negtive:
            tmp = 1 / tmp
        return tmp
        
        
        
#         x^100
        
#         x^50 x^50
        
        
        
#         x^n = x^(n/2) * x^(n/2)      n is even
#         x^n = x^(n//2) * x^(n//2) * x  n is odd
        
          