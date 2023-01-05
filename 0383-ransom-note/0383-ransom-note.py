class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr = [0] * 26

        for x in magazine:    # 记录 magazine里各个字符出现次数
            arr[ord(x) - ord('a')] += 1

        for x in ransomNote:  # 在arr里对应的字符个数做--操作
            if arr[ord(x) - ord('a')] == 0:  # 如果没有出现过直接返回
                return False
            else:
                arr[ord(x) - ord('a')] -= 1
        
        return True