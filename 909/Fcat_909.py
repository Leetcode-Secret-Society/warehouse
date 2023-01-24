from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        bfs_queue = deque()
        bfs_queue.append((1, 0))
        goal = len(board) * len(board)
        checked = [False] * goal
        checked[0] = False

        def find_next_move(index):
            index -= 1
            y = len(board) - 1 - (index // len(board))
            from_left = y % 2 == (len(board) - 1) % 2
            if from_left:
                x = index % len(board)
            else:
                x = len(board) - 1 - index % len(board)

            return board[y][x]

        while bfs_queue:
            pos, moves = bfs_queue.popleft()
            for i in range(1, 7):
                next_move = find_next_move(pos + i)
                if next_move == -1:
                    next_move = pos + i
                if next_move == goal:
                    return moves + 1
                if not checked[next_move]:
                    bfs_queue.append((next_move, moves + 1))
                    checked[next_move] = True
        return -1


print(Solution().snakesAndLadders([[1, 1, -1], [1, 1, 1], [-1, 1, 1]]))
