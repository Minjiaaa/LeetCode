class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        res = (0, 0)
        for mid in range(len(s)):
            res = max(res, self.get_palindrome_from(s, mid, mid))
            res = max(res, self.get_palindrome_from(s, mid, mid + 1))
        return s[res[1]: res[0] + res[1]]
    def get_palindrome_from(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1, left + 1