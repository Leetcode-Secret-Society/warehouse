from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    matrix[i][j] += matrix[i - 1][j]

        result = 0
        for row in matrix:
            row.sort(reverse=True)
            for i in range(len(row)):
                result = max(result, row[i] * (i + 1))
        return result


print(Solution().largestSubmatrix([[1, 0], [1, 0], [0, 1], [0, 1]]))
