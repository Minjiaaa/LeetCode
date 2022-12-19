class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        path = []
        res = []
        if len(digits) == 0:
            return []
        
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
        
        def helper(digits, index):
            if index == len(digits):
                res.append(path[:])
                return res
            
            letters = phone[digits[index]]
            
            for letter in letters:
                path.append(letter)
                helper(digits, index + 1)
                path.pop()
        
        helper(digits, 0)
        
        for i, path in enumerate(res):
            res[i] = "".join(path)
        
        return res
