class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        max_col = len(grid[0])
        max_row = len(grid)
        def dfs(row, col) :
            if row < 0 or col < 0 or row >= max_row or col >= max_col or grid[row][col] == "0":
                return
            grid[row][col] = "0" #clever
            dfs(row+1, col)
            dfs(row, col+1)
            dfs(row-1, col)
            dfs(row, col-1)
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                val = grid[row][col]
                if val == "1":
                    result += 1
                    dfs(row , col)
        return result
