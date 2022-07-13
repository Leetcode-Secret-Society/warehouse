class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        queue = deque()
        queue.append((0,0))
        grid[0][0] = 1
        
        while len(queue) > 0:
            row, col = queue.popleft()
            distance = grid[row][col]
            if (row, col) == (max_row, max_col):
                return distance
            for direction_row, direction_col in directions:
                to_go = (row + direction_row, col + direction_col)
                if to_go[0] > -1 and to_go[0] <= max_row and to_go[1] > -1 and to_go[1] <= max_col: #boundary
                    if grid[to_go[0]][to_go[1]] == 0: #possible path
                        grid[row + direction_row][col + direction_col] = distance + 1
                        queue.append(to_go)
        return -1
