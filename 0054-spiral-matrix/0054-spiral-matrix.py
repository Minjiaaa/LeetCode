class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []
        rows = len(matrix)
        cols = len(matrix[0])
        up = left = 0
        right = cols - 1
        down = rows - 1
        
        while len(res) < rows * cols:
            for col in range(left, right + 1):
                res.append(matrix[up][col])
            
            for row in range(up + 1, down + 1):
                res.append(matrix[row][right])
            
            if up != down:
                for col in range(right - 1, left - 1, -1):
                    res.append(matrix[down][col])
            
            if left != right:
                for row in range(down - 1, up, -1):
                    res.append(matrix[row][left])
                
                left += 1
                right -= 1
                up += 1
                down -= 1
        return res