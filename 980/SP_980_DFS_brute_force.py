class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        zero_count = 0
        wall_count = 0
        start_pos = (0,0)
        end_pos = (0,0)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    zero_count += 1
                elif grid[i][j] == 1:
                    zero_count += 1
                    start_pos = (i, j)
                elif grid[i][j] == 2:
                    end_pos = (i, j)
                else:
                    wall_count += 1

        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        
        #[[1,0,0,0],
        #[0,0,0,0],
        #[0,0,2,-1]]

        def dfs(grid: List[List[int]], pos: (int,int), zero_count: int) -> int:
            if pos[0] < 0 or pos[0] == len(grid) or pos[1] < 0 or pos[1] == len(grid[pos[0]]):
                return 0 #boundary
            if grid[pos[0]][pos[1]] == -1:
                return 0 #wall
            if grid[pos[0]][pos[1]] == 2:
                if zero_count == 0:
                    return 1 #end
                else:
                    return 0 #wrong path
            grid[pos[0]][pos[1]] = -1 #visited
            path_result = 0
            for direction in directions:
                path_result += dfs(grid, (pos[0] + direction[0], pos[1] + direction[1]), zero_count - 1)
            grid[pos[0]][pos[1]] = 0 #reset
            return path_result
        
        return dfs(grid, start_pos, zero_count)
                
