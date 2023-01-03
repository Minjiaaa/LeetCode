class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        cur = []
        def helper(n, x):
            if cur:
                res.append(cur[:] + [n])
                # print(res)
                # print(n)
            
            for i in range(x, int(pow(n, 0.5)) + 1):
                if n % i == 0:
                    cur.append(i)
                    helper(n // i, i)
                    cur.pop()
        helper(n, 2)
        return res
        
        """这么写超出内存限制"""
#         res = []
#         path = []
#         factors = []
        
#         # 如何判断是否为质数
#         # 先构造出可以进行回溯的数组
#         for i in range(2, n - 1):
#             if n % i == 0:
#                 factors.append(i)
    
#         if not factors:
#             return []
        
#         def helper(n, factors, start_index, cur_product):
#             if cur_product == n:
#                 res.append(path[:])
#                 return
            
#             for i in range(len(factors)):
#                 path.append(factors[i])
#                 cur_product *= factors[i]
#                 helper(n, factors, i, cur_product)
#                 path.pop()
#                 cur_product /= factors[i]
        
        
#         helper(n,factors, 0, 1)
#         return res
       
    
            