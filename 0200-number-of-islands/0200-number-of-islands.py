DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0,1)]
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # # 特殊情况处理
        # if not grid or not grid[0]:
        #     return 0
        
        islands = 0
        #记录某点是否被BFS过，如果之前已经被BFS过，不应该再次被BFS
        visited = set()

        # 遍历矩阵中的每一个点
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 如果为海洋，无需BFS
                # 如果该点已经被visited, 无需做荣誉遍历，重复计算
                if grid[i][j] == "1" and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1
        return islands

    # 从一块土地出发，通过BFS，遍历整个岛屿
    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            # 遍历上下左右四个方向
            for x_, y_ in DIRECTIONS:
                next_x = x + x_
                next_y = y + y_
                if not self.is_valid(grid, next_x, next_y, visited):
                    continue
                #print(grid[x][y])
                #print(next_x, next_y)
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))

    # 判断一个点是否可以被BFS
    def is_valid(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])
            #如果出界，返回false
        if not (0 <= x < n and 0 <= y < m):
            return False
        # 如果已经BFS过，不要再次BFS，避免： 1. 死循环 2. 冗余的BFS变量
        if (x, y) in visited:
            return False
        # 如果是1， 则为true；如果0， 则为False
        return grid[x][y] == "1"