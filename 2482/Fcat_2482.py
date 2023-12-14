from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        height = len(grid)
        width = len(grid[0])
        result = [[0] * width for _ in range(height)]
        row_sums = [0] * height
        column_sums = [0] * width

        for y in range(height):
            for x in range(width):
                if grid[y][x] == 1:
                    row_sums[y] += 1
                    column_sums[x] += 1

        for y in range(height):
            for x in range(width):
                result[y][x] = 2 * row_sums[y] + 2 * column_sums[x] - height - width

        return result