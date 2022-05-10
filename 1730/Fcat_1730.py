from heapq import heappop, heappush
from typing import List


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '*':
                    start = (x, y)
                    break
        traveled = [[False] * len(grid[0]) for _ in range(len(grid))]
        path = []
        traveled[start[1]][start[0]] = True
        heappush(path, (0, start))
        while path:
            step, coordinator = heappop(path)
            x, y = coordinator
            if grid[y][x] == '#':
                return step
            for cord_x, cord_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_x = x + cord_x
                next_y = y + cord_y
                if next_x < 0 or next_x >= len(grid[0]) or next_y < 0 or next_y >= len(grid) or grid[next_y][
                    next_x] == 'X' or traveled[next_y][next_x]:
                    continue
                traveled[next_y][next_x] = True
                heappush(path, (step + 1, (next_x, next_y)))
        else:
            return -1


print(Solution().getFood(grid=[["O", "*"], ["#", "O"]]))
