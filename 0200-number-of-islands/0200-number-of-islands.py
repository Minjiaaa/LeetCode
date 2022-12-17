class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        
        def bfs(r, c):
            # grid[r][c] = "0"
            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))
            while q:
                r, c = q.popleft()
                for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    rd, cd = r + x, c + y #变量更新要注意
                    if (0 <= rd < rows and 
                        0 <= cd < cols and 
                        grid[rd][cd] == "1" and 
                        (rd, cd) not in visit):
                        q.append((rd, cd))
                        # grid[rd][cd] = 0
                        visit.add((rd, cd))
                        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands
                    
        
#     def numIslands(self, grid: List[List[str]]) -> int:
#         def bfs(i, j):
#             grid[i][j] = '0'
#             q = deque([(i, j)])
#             while q:
#                 i, j = q.popleft()
#                 for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
#                     x, y = i + a, j + b
#                     if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
#                         q.append((x, y))
#                         grid[x][y] = 0

#         m, n = len(grid), len(grid[0])
#         ans = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     bfs(i, j)
#                     ans += 1
#         return ans