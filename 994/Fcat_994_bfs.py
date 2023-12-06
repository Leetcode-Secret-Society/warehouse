from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        rotten_queue = deque()

        last_minute = 0

        for y in range(height):
            for x in range(width):
                if grid[y][x] == 2:
                    rotten_queue.append((x, y, 0))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while rotten_queue:
            x, y, last_minute = rotten_queue.popleft()
            grid[y][x] = 0
            for d_x, d_y in directions:
                neighbor_x = x + d_x
                neighbor_y = y + d_y
                if 0 <= neighbor_x < width and 0 <= neighbor_y < height:
                    if grid[neighbor_y][neighbor_x] == 1:
                        grid[neighbor_y][neighbor_x] = 0
                        rotten_queue.append((neighbor_x, neighbor_y, last_minute + 1))

        for y in range(height):
            for x in range(width):
                if grid[y][x] == 1:
                    return -1

        return last_minute
