class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, longest = 0, 0
        for middle in range(len(s)):
            # add
            left, right = middle, middle
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if longest < right - left - 1:
                longest = right - left - 1 # right = left + 1 - 2
                start = left + 1
            
            left, right = middle, middle + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if longest < right - left - 1:
                longest = right - left - 1 # right = left + 1 - 2
                start = left + 1
            
        return s[start: start + longest]
            