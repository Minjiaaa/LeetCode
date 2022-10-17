class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        prev = 2
        prePre = 1
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            for i in range(3, n + 1):
                res = prev + prePre
                prePre = prev
                prev = res
        return res
                
            
        