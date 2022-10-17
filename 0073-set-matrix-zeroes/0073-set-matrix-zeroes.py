class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(1)
        m, n = len(matrix), len(matrix[0])
        zeroFirstRow = any(matrix[0][c] == 0 for c in range(n))
        zeroFirstCol = any(matrix[r][0] == 0 for r in range(m))
        
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[0][c] = matrix[r][0] = 0
        
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if zeroFirstRow:
            for c in range(n):
                matrix[0][c] = 0
            
        if zeroFirstCol:
            for r in range(m):
                matrix[r][0] = 0

       