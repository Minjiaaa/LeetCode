class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        res = []
        '''
        递归用于纵向遍历
        for循环用于横向遍历
        当切割线迭代至字符串末尾，说明找到一种方法
        类似组合问题，为了不重复切割同一位置，需要start_index来做标记下一轮递归的起始位置(切割线)
        '''
        def helper(s, index):
            if index == len(s):
                res.append(path[:])
                return
            # 单层递归逻辑
            for i in range(index, len(s)):
                tmp = s[index: i + 1]
                if tmp == tmp[::-1]: # 若反序和正序相同，意味着这是回文串
                    path.append(tmp)
                    helper(s, i + 1)
                    path.pop()
                else:
                    continue
        
        helper(s, 0)
        return res
                
        
        
            
        
        
        
        
        