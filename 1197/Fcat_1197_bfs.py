from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        target_x = abs(x)
        target_y = abs(y)
        if target_x == 1 and target_y == 1:
            return 2
        bfs = deque()
        bfs.append((0, 0, 0))
        directions = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
        moved = set()
        while bfs:
            cur_x, cur_y, moves = bfs.popleft()
            if (cur_x, cur_y) in moved:
                continue
            moved.add((cur_x, cur_y))
            if cur_x < 0 or cur_y < 0:
                continue
            if cur_x == target_x and cur_y == target_y:
                return moves
            for d_x, d_y in directions:
                bfs.append((cur_x+d_x, cur_y+d_y, moves + 1))