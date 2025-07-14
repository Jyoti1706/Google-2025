from typing import List
from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        row_count = len(grid)
        col_count = len(grid[0])
        queue = deque()
        start=(0, 0, k)
        queue.append(start)
        visited = set()
        visited.add(start)
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        steps = 0
        while queue:
            level = len(queue)
            while level > 0:
                row, column, allowed = queue.popleft()
                if row == row_count - 1 and column == col_count-1:
                    return steps
                for direction in directions:
                    new_row = row + direction[0]
                    new_col = column + direction[1]
                    if (col_count > new_col >= 0) and (0 <= new_row < row_count):
                        if grid[new_row][new_col] == 0 and (new_row, new_col, allowed) not in visited:
                            queue.append((new_row, new_col, allowed))
                            visited.add((new_row, new_col, allowed))
                        elif grid[new_row][new_col] == 1 and allowed > 0 and (
                            new_row, new_col, allowed - 1) not in visited:
                            queue.append((new_row, new_col, allowed - 1))
                            visited.add((new_row, new_col, allowed - 1))
                level -= 1
            steps += 1
        return -1


grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
k = 1
obj = Solution()
print(obj.shortestPath(grid, k))

grid = [[0,1,1],[1,1,1],[1,0,0]]
k = 1
print(obj.shortestPath(grid, k))