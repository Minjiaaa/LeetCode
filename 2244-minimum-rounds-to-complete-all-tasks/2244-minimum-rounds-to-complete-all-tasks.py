class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = {}
        for task in tasks:
            if task in count:
                count[task] += 1
            else:
                count[task] = 1
            
        res = 0
        
        for key in count.values():
            if key == 1:
                return -1
                
            if key % 3 == 0:
                res += key // 3
            elif key % 3 == 2:
                res = res + key // 3 + 1
    
            elif key != 1 and key % 3 == 1 :
                res = res + (key - 3) // 3 + 2

        return res
        