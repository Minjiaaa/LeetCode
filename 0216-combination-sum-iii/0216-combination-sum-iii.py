class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        
        def helper(n, k, start_index):
            if sum(path) == n and len(path) == k:
                res.append(path[:])
                return
            
            for i in range(start_index, 10):
                path.append(i)
                helper(n, k, i + 1)
                path.pop()
        
        helper(n, k, 1)
        return res