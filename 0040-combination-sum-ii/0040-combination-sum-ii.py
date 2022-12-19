class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        #visit = set()
        candidates.sort() 
        # 为了将重复的数字都放到一起，所以先进行排序
        '''
        类似于求三数之和，求四数之和，为了避免重复组合，需要提前进行数组排序
        '''
        used = [False] * len(candidates)
        
        def helper(candidates, target, index):
            # 使用tuple（hashable）,会超时，所以只能对每一个元素进行进行去重操作
            # str_path = tuple(path) 
            if sum(path) > target: #or str_path in visit: # 剪枝，同39.组合总和
                return
            
            if sum(path) == target:
                # visit.add(str_path)
                res.append(path[:])
                return
            
            for i in range(index, len(candidates)):
            # 不使用used数组进行去重的方式1：//跳过同一树层使用过的元素
                # if i > index and candidates[i] == candidates[i-1]:
                #     continue 
            
            # 不使用used数组进行去重的方式2:判断这个candiates[i]是不是path中出现的第一个元素
                # if i != 0 and candidates[i] == candidates[i-1] and not path:
                #     continue
            
            # 使用used数组判断是否出现过：加标志数组，用来辅助判断同层节点是否已经遍历
                # 若数组中前后元素值相同，但前者却未被使用(used == False)，说明是for loop中的同一树层的相同元素情况
                    # used[i - 1] == true，说明同一树枝candidates[i - 1]使用过
                    # used[i - 1] == false，说明同一树层candidates[i - 1]使用过
                if i > 0 and candidates[i] == candidates[i-1] and used[i - 1] == False:
                    continue
                
                used[i] = True
                path.append(candidates[i])
                helper(candidates, target, i + 1) # i+1 代表当前组内元素只选取一次
                used[i] =False # 回溯，为了下一轮for loop
                path.pop() # 回溯，为了下一轮for loop


        # 进行去重的方式3
        # for i, num in enumerate(candidates):
        #     if num in visit:
        #         continue
        #     visit.add(num)
        helper(candidates, target, 0)
            
        return res
        
        