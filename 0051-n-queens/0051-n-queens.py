class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for i in range(n)]
        res = []
        
        def isValid(board, row, col):
            #同一列
            for i in range(len(board)):
                if board[i][col] =='Q':
                    #print('here?')
                    return False
              # 判断左上角是否冲突
# 相当于遍历了前面所有的方块，所以不能用for循环写。
#             for i in range(row-1, -1, -1):
#                 for j in range(col-1, -1, -1):
#                     if board[i][j] == 'Q':
#                         print('herere?')
#                         return False
            
#             for i in range(row -1, -1, -1):
#                 for j in range(col + 1, len(board)):
#                     if board[i][j] == 'Q':
#                         print('hererere?')
#                         return False
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1
            
            i = row - 1
            j = col + 1
            while i >= 0 and j < len(board):
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            return True
        
        def helper(board, row, n):
            #print(row, n)
            if row == n:
                temp_res = []
                for temp in board:
                    temp_str = ''.join(temp) #转换成字符串
                    temp_res.append(temp_str) #对于每一个可能的结果进行形式上的处理
                #print(temp_res)
                res.append(temp_res) #将单一结果加入结果集
                
            for col in range(n):
                if not isValid(board, row, col):
                    continue
                board[row][col] = 'Q'
                helper(board, row + 1, n)
                board[row][col] = '.'
                
        
        helper(board, 0, n)
        return res
        