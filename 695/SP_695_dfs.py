class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        num_row, num_col = len(grid), len(grid[0])
        visited = [[0] * num_col for _ in range(num_row)]
        islands = defaultdict(int)
        
        def dfs(grid: List[List[int]], visited: List[List[int]], current_row:int, current_col:int, source):
            global result
            if visited[current_row][current_col] != 0:
                return
            visited[current_row][current_col] = 2
            # print(str(current_row)+"-"+str(current_col))
            
            if grid[current_row][current_col] == 1:
                islands[source] += 1
                # result = max(islands[source], result)
            else:
                return
            if current_row + 1 < num_row:
                dfs(grid, visited, current_row+1, current_col, source)
            if current_row - 1 >= 0:
                dfs(grid, visited, current_row-1, current_col, source)
            if current_col + 1 < num_col:
                dfs(grid, visited, current_row, current_col+1, source)
            if current_col - 1 >= 0:
                dfs(grid, visited, current_row, current_col-1, source)
        
        for row in range(num_row):
            for col in range(num_col):
                dfs(grid, visited, row, col, str(row)+"-"+str(col))
            # print(result)
        for key in islands:
            result = max(result, islands[key])
        
        # print(visited)
        # print(islands)
        return result
