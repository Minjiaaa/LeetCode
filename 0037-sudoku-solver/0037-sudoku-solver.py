class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(board, row, col, val):
            for i in range(9):
                if board[row][i] == str(val):
                    return False
            
            for j in range(9):
                if board[j][col] == str(val):
                    return False
            
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == str(val):
                        return False
                    
            return True
        
        def helper(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] != '.':
                        continue
                    for k in range(1, 10):
                        if isValid(board, i, j, k):
                            board[i][j] = str(k)
                            if helper(board):
                                return True
                            board[i][j] = '.'
                    return False
            return True
        helper(board)