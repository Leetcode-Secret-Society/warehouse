from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        island_count = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def remove_island(island_x: int, island_y: int) -> None:
            remove_queue = deque()
            remove_queue.append((island_x, island_y))
            while remove_queue:
                x, y = remove_queue.pop()
                grid[y][x] = "0"
                for d_x, d_y in directions:
                    neighbor_x, neighbor_y = x + d_x, y + d_y
                    if 0 <= neighbor_x < width and 0 <= neighbor_y < height:
                        if grid[neighbor_y][neighbor_x] == "1":
                            remove_queue.append((neighbor_x, neighbor_y))

        for y in range(height):
            for x in range(width):
                if grid[y][x] == "1":
                    island_count += 1
                    remove_island(x, y)

        return island_count
