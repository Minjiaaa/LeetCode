class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12: return []  # 超出最长可能长度

        path = []
        res = []
        max_len = len(s)

        def backtrack(start_idx):
            if len(path) == 4:  # 最多只能有4个片段
                if start_idx == max_len:  # 有可能 start_idx 没遍历到最后一个数字，只有到了才是有效的
                    res.append('.'.join(path[:]))  # 加入 dot
                return

            # 横向遍历是找出一个有效片段，因为最大值255所以可以是1个数到3个数，所以+3，另外这里多了len(s)是为了防止指针溢出
            for idx in range(start_idx, min(start_idx + 3, max_len)):
                nums = s[start_idx:idx + 1]  # 获取当前片段，注意要+1
                path.append(nums)
                # 判断当前片段有效：保证0~255且没有前导0
                if int(nums) <= 255 and (start_idx == idx or s[start_idx] != '0'):
                    backtrack(idx + 1)  # 纵向遍历，获取下一个片段
                path.pop()  # 回溯，丢掉最后加入的片段
        
        backtrack(0)
        return res
        