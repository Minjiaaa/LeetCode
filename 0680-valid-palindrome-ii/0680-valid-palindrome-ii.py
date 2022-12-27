class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_isPalindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return check_isPalindrome(s, i, j - 1) or check_isPalindrome(s, i + 1, j)
            i += 1
            j -= 1
    
        return True
"""九章的代码是啥意思？"""
#     def validPalindrome(self, s: str) -> bool:
#         if s is None:
#             return False
#         left, right = self.findDifference(s, 0, len(s) - 1)
#         if left == right:
#             return True
        
#         return self.isPalindrome(s, left + 1, right) or\
#                 self.isPalindrome(s, left, right - 1)
        
#     def isPalindrome(self, s, left, right):
#         left, right = self.findDifference(s, left, right)
#         return left == right
    
#     def findDifference(self, s, left, right):
#         while left < right:
#             if s[left] != s[right]:
#                 return left, right
#             left += 1
#             right -= 1
#         return left, right
        
