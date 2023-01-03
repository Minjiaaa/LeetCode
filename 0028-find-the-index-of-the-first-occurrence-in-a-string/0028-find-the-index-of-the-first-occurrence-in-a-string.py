class Solution:
    def strStr(self, hay: str, nee: str) -> int:
#         if not haystack:
#             return 0
        
#         for i in range(len(haystack) - len(needle) + 1): # haystack == needle
#             for j in range(len(needle)):
#                 if haystack[i + j] != needle[j]:
#                     break
#             else: # break和else只执行一个
#                 return i
        
#         return -1 
        if not hay:
            return 0
        
        power = 10 ** 8
        hash_nee = 0
        size = len(nee)
        hash_hay = 0
        
        for n in nee:
            hash_nee = (hash_nee * 31 + ord(n)) % power
            
        for i in range(len(hay)):
            hash_hay = (hash_hay * 31 + ord(hay[i])) % power
            if i < size - 1:
                continue
            if hash_hay == hash_nee:
                return i - size + 1
            hash_hay = (hash_hay -  ord(hay[i-size+1]) * (31 ** (size-1)) ) % power
            
            if hash_hay < 0:
                hash_hay += power
        
        return -1