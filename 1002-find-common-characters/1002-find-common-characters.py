class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
#         dict = {}
        
#         for i in range(len(words):
#             for j in words[i]:
#                 dict[j] = dict
#         #不知道怎么处理无限循环
        res = []
        for c in set(words[0]):
            count = words[0].count(c)
            occurrences = 1
            for i in range(1, len(words)):
                if c in words[i]:
                    count = min(count, words[i].count(c))
                    occurrences += 1
                else:
                    break
            if occurrences == len(words):
                for i in range(count):#这个不太懂
                    res.append(c)
        
        return res
            
            
        