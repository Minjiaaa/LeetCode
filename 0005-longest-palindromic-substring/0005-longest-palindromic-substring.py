class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None:
            return None
        
        for length in range(len(s), 0, -1):
            for i in range(len(s) - length + 1):
                if self.is_palindrome(s, i, i + length - 1):
                    return s[i : i + length]
        return ""
    
    # 判断是否为回文串的子函数
    def is_palindrome(self, s, left, right):
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
            
        return left >= right
        