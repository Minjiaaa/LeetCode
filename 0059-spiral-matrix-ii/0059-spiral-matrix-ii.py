class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0] * n for _ in range(n)]
        start_x, start_y = 0, 0
        loop = n // 2
        mid = n // 2
        num = 1
        
        for offset in range(1, loop + 1):
            # 从左到右
            for j in range(start_y, n - offset):
                nums[start_x][j] = num
                num += 1
            for i in range(start_x, n - offset):
                nums[i][n - offset] = num
                num += 1
            for j in range(n - offset, start_y, -1):
                nums[n - offset][j] = num
                num += 1
            for i in range(n - offset, start_x, -1):
                nums[i][start_y] = num
                num += 1
            start_x += 1
            start_y += 1
        
        if n % 2 == 1:
            nums[mid][mid] = num
        
        return nums