from collections import deque
from typing import List


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        path = deque()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '*':
                    path.append((0, x, y))
                    break

        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while path:
            step, x, y = path.popleft()
            for cord_x, cord_y in dir:
                next_x = x + cord_x
                next_y = y + cord_y
                if 0 <= next_x < len(grid[0]) and 0 <= next_y < len(grid) and grid[next_y][next_x] in ('O', '#'):
                    if grid[next_y][next_x] == '#':
                        return step + 1
                    grid[next_y][next_x] = None
                    path.append((step + 1, next_x, next_y))
        else:
            return -1


print(Solution().getFood(grid=[["O", "*"], ["#", "O"]]))
