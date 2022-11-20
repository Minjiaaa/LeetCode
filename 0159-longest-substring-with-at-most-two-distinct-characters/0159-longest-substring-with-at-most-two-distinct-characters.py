class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        table = {}
        left = 0
        maxLen = 0
        for right in range(0, n):
            table[s[right]] = table.get(s[right], 0) + 1
            while left < right and len(table) > 2:
                table[s[left]] -= 1
                if table[s[left]] == 0:
                    del table[s[left]]
                left += 1
            maxLen = max(maxLen, right - left + 1)
        return maxLen
    
        # maxSub = 0
        # for i in range(n):
        #     table = {}
        #     for j in range(i, n):
        #         table[s[j]] = True
        #         if len(table) >= 3:
        #             break
        #         else:
        #             maxSub = max(maxSub, j - i + 1)
        # return maxSub