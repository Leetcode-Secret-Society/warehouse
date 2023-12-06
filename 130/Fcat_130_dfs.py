from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        height = len(board)
        width = len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def reseve_O(x, y):
            if x < 0 or x >= width or y < 0 or y >= height or board[y][x] == "X" or board[y][x] == "R":
                return
            board[y][x] = "R"
            for d_x, d_y in directions:
                reseve_O(x + d_x, y + d_y)

        for y in range(height):
            reseve_O(0, y)
            reseve_O(width - 1, y)

        for x in range(width):
            reseve_O(x, 0)
            reseve_O(x, height - 1)

        for y in range(height):
            for x in range(width):
                if board[y][x] == "O":
                    board[y][x] = "X"
                elif board[y][x] == "R":
                    board[y][x] = "O"