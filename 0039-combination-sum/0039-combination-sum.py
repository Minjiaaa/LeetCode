class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        
        def helper(candidates, target, index):
            if sum(path) > target:
                return
            
            if sum(path) == target:
                res.append(path[:])
                return
        
            for i in range(index, len(candidates)):
                if sum(path) + candidates[i] > target:
                    continue
                else:
                    path.append(candidates[i])
                    print(path)
                    helper(candidates, target, i)
                    path.pop()
            
        helper(candidates, target, 0)
        return res
                
                
        