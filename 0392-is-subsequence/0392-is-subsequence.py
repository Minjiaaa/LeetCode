class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1 #I不变，j一直往后面移动找符合的值
            
        return i == len(s) #如果i能到达字符串末尾。说明是subsequence