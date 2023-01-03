class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        
        return -1