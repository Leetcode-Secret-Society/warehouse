from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        edge_lands = []
        for x in range(len(grid[0])):
            if grid[0][x] == 1:
                edge_lands.append((x, 0))
            if grid[-1][x] == 1:
                edge_lands.append((x, len(grid) - 1))
        for y in range(len(grid)):
            if grid[y][0] == 1:
                edge_lands.append((0, y))
            if grid[y][-1] == 1:
                edge_lands.append((len(grid[0])-1, y))
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(x, y):
            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
                return
            if grid[y][x] == 0:
                return
            grid[y][x] = 0
            for dir_x, dir_y in directions:
                dfs(x+dir_x, y+dir_y)

        for x, y in edge_lands:
            dfs(x,y)

        lands = 0
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[y][x] == 1:
                    lands += 1

        return lands

print(Solution().numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0]]))
