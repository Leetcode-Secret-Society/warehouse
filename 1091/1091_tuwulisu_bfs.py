class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def in_grid(position):
            m = len(grid)
            n = len(grid[0])
            return position[0]>=0 and position[0]<m and position[1]>=0 and position[1]<n
        directions = [(1,-1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, 0), (-1, 1), (-1, -1)]
        if grid[0][0]==1:
            return -1
        if grid[0][0]==0 and m==1 and n==1:
            return 1
        queue = [(0, 0)]
        step_count = 1
        while queue:
            new_queue = []
            for cell in queue:
                grid[cell[0]][cell[1]] = 1
            while queue:
                position = queue.pop()
                for direction in directions:
                    next_position = (position[0]+direction[0], position[1]+direction[1])
                    if in_grid(next_position) and grid[next_position[0]][next_position[1]]==0:
                        grid[next_position[0]][next_position[1]]=1
                        new_queue.append(next_position)
                        if next_position == (m-1, n-1):
                            return step_count + 1
            queue = new_queue
            step_count+=1
        return -1
                    
