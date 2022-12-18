class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        res = []
                
        def helper(n, k, start_index):
            if len(path) == k:
                res.append(path[:]) #为什么一定要copy一遍path？
                return

            for i in range(start_index, n + 1):
                path.append(i)
                helper(n, k, i + 1)
                path.pop()     
        
        helper(n, k, 1)
        return res