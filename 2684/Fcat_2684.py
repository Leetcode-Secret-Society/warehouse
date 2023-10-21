from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        dp = [[-1] * len(grid[0]) for _ in range(len(grid))]

        def get_pos_max_moves(x, y, last_value):
            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
                return -1
            if dp[y][x] >= 0:
                return dp[y][x]
            cur_value = grid[y][x]
            if cur_value <= last_value:
                return -1

            max_moves = max(get_pos_max_moves(x + 1, y - 1, cur_value), get_pos_max_moves(x + 1, y, cur_value),
                            get_pos_max_moves(x + 1, y + 1, cur_value))
            dp[y][x] = max_moves + 1
            return dp[y][x]

        result = 0
        for i in range(len(grid)):
            result = max(result, get_pos_max_moves(0, i, 0))
        return result
