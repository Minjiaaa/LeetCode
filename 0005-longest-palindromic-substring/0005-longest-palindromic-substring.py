class Solution:
    def longestPalindrome(self, s: str) -> str:
        minLen1 = float('-inf')
        minLen2 = float('-inf')
        maxStr = ""
        for i in range(len(s)):
            left = right = i
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            # print(f'left = {left}')
            # print(f'right = {right}')
            # resLeft1 = left
            # resRight1 = right
            if right - left - 1 > len(maxStr):
                maxStr = s[left+1:right]
            # minLen1 = max(minLen1, right - left - 1)
        
        for j in range(len(s)):
            left = j
            right = j + 1
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            # print(f'left = {left}')
            # print(f'right = {right}')
            # resLeft2 = left
            # resRight2 = right
            # minLen2 = max(minLen2, right - left - 1)
            if right - left - 1 > len(maxStr):
                maxStr = s[left+1:right]
            
        return maxStr
        
#         if minLen1 <= minLen2:
#             return s[resLeft2 + 1: resRight2]
#         else:
#             return s[resLeft1 + 1: resRight1]
            
            
            
        