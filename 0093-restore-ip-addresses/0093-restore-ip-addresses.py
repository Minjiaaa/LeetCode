class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        '''
        本质切割问题使用回溯搜索法，本题只能切割三次，所以纵向递归总共四层
        因为不能重复分割，所以需要start_index来记录下一层递归分割的起始位置
        添加变量point_num来记录逗号的数量[0,3]
        '''
        # 判断字符串s在左闭又闭区间[start, end]所组成的数字是否合法
        def isvalid(s, start, end):
            if start > end:
                return False
            # 段位以0为开头的数字不合法
            if s[start] == '0' and start != end:
                return False
            
            if not 0 <= int(s[start:end+1]) <= 255:
                return False
            
            return True
        
        
        def helper(s, index, point_num):
            #Base case
            if point_num == 3:
                if isvalid(s, index, len(s) - 1): #这里如何判断s的长度
                    res.append(s[:])
                return
            
            for i in range(index, len(s)):
                # [index, i]就是被截取的子串
                if isvalid(s, index, i):
                    s = s[:i+1] + '.' + s[i+1:]
                    helper(s, i + 2, point_num + 1)
                        # 在填入.后，下一子串起始后移2位
                    s = s[:i+1] + s[i+2:] #回溯
                else:
                    break
        if len(s) > 12:
            return []
        helper(s, 0, 0)
        return res
            
            
        