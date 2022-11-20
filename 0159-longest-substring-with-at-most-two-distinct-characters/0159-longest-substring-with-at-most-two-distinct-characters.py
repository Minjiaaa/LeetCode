class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        left = 0
        cnt = {}
        maxLen = 0
        for right in range(len(s)):
            cnt[s[right]] = cnt.get(s[right], 0) + 1
            while left < right and len(cnt) > 2:
                cnt[s[left]] -= 1
                
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
                left += 1
            
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen
    
    # e, c, e, b, a
    # right = 0, cnt = {'e': 1} maxlen = 1
    # right = 1, cnt = {'e' : 1, 'c' : 1}, maxLen = 2
    # right = 2, cnt = {'e' : 2, 'c' : 1}, maxLen = 3
    # right = 3, cnt = {'e' : 2, 'c' : 1, 'b' : 1}, cnt = {'e' : 1, 'c' : 1, 'b' : 1} 
    #             left = 1, cnt = {'e' : 1, 'c' : 0, 'b' : 1} -> cnt = {'e' : 1, 'b' : 1}
    #             left = 2, maxLen = 3
                
    
    
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