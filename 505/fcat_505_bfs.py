from typing import List
from heapq import heappop, heappush


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        passed = [[[0] * 2 for _ in range(len(maze[0]))] for _ in range(len(maze))]
        next_start = []
        heappush(next_start, [0, start[0], start[1]])
        while next_start:
            step, y, x = heappop(next_start)
            if y == destination[0] and x == destination[1]:
                return step

            next_direction = []
            if passed[y][x][0] == 0:
                next_direction.extend([[0, 1], [0, -1]])
            if passed[y][x][1] == 0:
                next_direction.extend([[1, 0], [-1, 0]])
            for next_dir in next_direction:
                next_step = step
                next_x = x
                next_y = y
                moved = False
                while len(maze[0]) > next_x >= 0 and len(maze) > next_y >= 0 and maze[next_y][next_x] != 1:
                    next_x += next_dir[0]
                    next_y += next_dir[1]
                    next_step += 1
                    moved = True
                if moved:
                    heappush(next_start, [next_step - 1, next_y - next_dir[1], next_x - next_dir[0]])

            passed[y][x] = [1, 1]

        return -1


print(Solution().shortestDistance([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],
                                  [0, 4], [4, 4]))
