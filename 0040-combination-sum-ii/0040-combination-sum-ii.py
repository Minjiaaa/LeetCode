class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        #visit = set()
        candidates.sort() # 为了将重复的数字都放到一起，所以先进行排序
        
        
        def helper(candidates, target, index):
            # str_path = tuple(path)
            if sum(path) > target: #or str_path in visit:
                return
            
            if sum(path) == target:
                # visit.add(str_path)
                res.append(path[:])
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                # if i != 0 and candidates[i] == candidates[i-1] and not path:
                #     continue
                path.append(candidates[i])
                helper(candidates, target, i + 1) # i+1 代表当前组内元素只选取一次
                path.pop()
        
        # for i, num in enumerate(candidates):
        #     if num in visit:
        #         continue
        #     visit.add(num)
        helper(candidates, target, 0)
            
        return res
        
        