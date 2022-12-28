DIRECTIONS = [(2, -1), (1, -2), (2, 1), (1, 2), (-1, 2), (-1, -2), (-2, -1), (-2, 1)]
class Solution:
    def minKnightMoves(self, a: int, b: int) -> int:
        queue = deque([(0, 0)])
        visited = set()
        visited.add((0, 0))
        distance = -1
        
        while queue:
            size = len(queue)
            distance += 1
            for i in range(size):
                x, y = queue.popleft()
                if x == a and y == b:
                    return distance
                for x_, y_ in DIRECTIONS:
                    next_x = x + x_
                    next_y = y + y_
                    if (next_x, next_y) in visited:
                        continue
                    queue.append((next_x, next_y))
                    visited.add((next_x, next_y))

  


        