from functools import cache


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        @cache
        def count_paths(x: int, y: int, moves: int) -> int:
            if x < 0 or x == n or y < 0 or y == m or moves == 0:
                return 0
            paths = 0

            if x == 0:
                paths += 1
            if x == n - 1:
                paths += 1
            if y == 0:
                paths += 1
            if y == m - 1:
                paths += 1

            for dir_x, dir_y in directions:
                paths += count_paths(x + dir_x, y + dir_y, moves - 1)
            return paths % (10 ** 9 + 7)

        return count_paths(startColumn, startRow, maxMove)