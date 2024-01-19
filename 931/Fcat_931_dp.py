from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                left_index = max(j - 1, 0)
                right_index = min(j + 1, n - 1)
                matrix[i][j] += min(matrix[i - 1][j], matrix[i - 1][left_index], matrix[i - 1][right_index])

        return min(matrix[-1])
