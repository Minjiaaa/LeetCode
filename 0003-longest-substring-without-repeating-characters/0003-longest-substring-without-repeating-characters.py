class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        
        left = 0
        cnt = {}
        maxLen = 0
        
        for right in range(n):
            cnt[s[right]] = cnt.get(s[right], 0) + 1
            
            #find the inappropriate condition
            while left < right and cnt[s[right]] > 1:
                cnt[s[left]] -= 1
                left += 1
                    
            maxLen = max(maxLen, right - left + 1)
            
        return maxLen
    
#     "abcabcbb"
    
#     left = 0
#     right = 0, cnt = {'a' : 1}, maxLen = 1
#     right = 1, cnt = {'a' : 1, 'b' : 1}, maxLen = 2
#     right = 2, cnt = {'a' : 1, 'b' : 1, 'c' : 1}, maxLen = 3
#     right = 3, cnt = {'a' : 2, 'b' : 1, 'c' : 1}, cnt = {'a' : 1, 'b' : 1, 'c' : 1}. left = 1, maxLen = 3
#     right = 4, cnt = {'a' : 1, 'b' : 2, 'c' : 1}, cnt = {'a' : 1, 'b' : 1, 'c' : 1}, left = 2, maxLen = 3
#     right = 5, cnt = {'a' : 1, 'b' : 2, 'c' : 2}, cnt = {'a' : 1, 'b' : 1, 'c' : 1}, left = 3, maxLen = 3
#     right = 6, cnt = {'a' : 1, 'b' : 2, 'c' : 1}, cnt = {'a' : 1, 'b' : 1, 'c' : 1}, left = 4, maxLen = 3
#     right = 7, cnt = 

# "pwwkew"
# left = 0
# right = 0, cnt = {p : 1}, maxLen = 1
# right = 1, cnt = {p : 1, w : 1}, maxLen = 1
# right = 2, cnt = {p : 1, w : 2}
    
        
        