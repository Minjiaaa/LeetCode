class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        path = []
        res = []

        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
    #      a.       b      c
    # d. e. f.    d e f         
    
        
        def helper(digits, index):
            if index == len(digits): #错误：index == len（digits）-1
                res.append(path[:])
                return res
#             for index in range(len(digits)):
#                 letters = phone[digits[index]]

#                 for letter in letters:
#                     path.append(letter)
#                     helper(digits, index + 1)
#                     path.pop()
            letters = phone[digits[index]]

            for letter in letters:
                path.append(letter)
                helper(digits, index + 1)
                path.pop()

        helper(digits, 0)
        
        for i, path in enumerate(res):
            res[i] = ''.join(path)
        
        return res
                    
                
            
            
        