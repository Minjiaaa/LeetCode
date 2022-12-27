class Solution:
    def isPalindrome(self, s: str) -> bool:
        #忽略大小写和非法字符的一些操作
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isValid(s[l]):
                l += 1
            while l < r and not self.isValid(s[r]):
                r -= 1
            if l < r and s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
    def isValid(self, char):
        return char.isdigit() or char.isalpha()
        