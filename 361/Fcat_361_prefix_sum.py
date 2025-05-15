from typing import List

WALL = "W"
ENEMY = "E"
EMPTY = "0"


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        width = len(grid[0])
        height = len(grid)

        from_left = [[0] * width for _ in range(height)]
        from_right = [[0] * width for _ in range(height)]
        from_top = [[0] * width for _ in range(height)]
        from_bottom = [[0] * width for _ in range(height)]

        # from_left
        enemies = 0
        for y in range(height):
            for x in range(width):
                if grid[y][x] == WALL:
                    enemies = 0
                elif grid[y][x] == ENEMY:
                    enemies += 1
                else:
                    from_left[y][x] = enemies
            enemies = 0

        # from_right
        for y in range(height):
            for x in range(width - 1, -1, -1):
                if grid[y][x] == WALL:
                    enemies = 0
                elif grid[y][x] == ENEMY:
                    enemies += 1
                else:
                    from_right[y][x] = enemies
            enemies = 0

        # from_top
        for x in range(width):
            for y in range(height):
                if grid[y][x] == WALL:
                    enemies = 0
                elif grid[y][x] == ENEMY:
                    enemies += 1
                else:
                    from_top[y][x] = enemies
            enemies = 0

        # from_bottom
        for x in range(width):
            for y in range(height - 1, -1, -1):
                if grid[y][x] == WALL:
                    enemies = 0
                elif grid[y][x] == ENEMY:
                    enemies += 1
                else:
                    from_bottom[y][x] = enemies
            enemies = 0

        dead_bodies = 0
        for y in range(height):
            for x in range(width):
                if grid[y][x] != EMPTY:
                    continue
                dead_bodies = max(dead_bodies, from_left[y][x] + from_right[y][x] + from_top[y][x] + from_bottom[y][x])

        return dead_bodies
