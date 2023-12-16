from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        height = len(grid)
        row_sums = [0] * height
        column_sums = [0] * width
        home_count = 0
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 1:
                    home_count += 1
                    column_sums[x] += 1
                    row_sums[y] += 1

        median = (home_count + 1) // 2
        current_count = 0
        meeting_point = [0, 0]
        for i in range(width):
            current_count += column_sums[i]
            if current_count >= median:
                meeting_point[0] = i
                break
        current_count = 0
        for i in range(height):
            current_count += row_sums[i]
            if current_count >= median:
                meeting_point[1] = i
                break

        result = 0
        for i in range(width):
            result += column_sums[i] * abs(i - meeting_point[0])

        for i in range(height):
            result += row_sums[i] * abs(i - meeting_point[1])

        return result
