class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m==0:
            return 0
        n = len(grid[0])
        prefix_x_matrix = []
        prefix_y_matrix = [[] for _ in range(m)]
        for row in grid:
            prefix_row = []
            current = 0
            for cell in row:
                if cell==1:
                    current+=1
                else:
                    current=0
                prefix_row.append(current)
            prefix_x_matrix.append(prefix_row)
        for x in range(n):
            current = 0
            for y in range(m):
                cell = grid[y][x]
                if cell==1:
                    current+=1
                else:
                    current=0
                prefix_y_matrix[y].append(current)
        #print(prefix_x_matrix)
        #print(prefix_y_matrix)
        max_len = 0
        for y in range(m):
            for x in range(n):
                cell = grid[y][x]
                possiable_max = min(prefix_x_matrix[y][x], prefix_y_matrix[y][x])
                for l in range(possiable_max, max_len, -1):
                    try:
                        if prefix_x_matrix[y-l+1][x]>=l and prefix_y_matrix[y][x-l+1]>=l:
                            break
                    except IndexError:
                        print(x,y,l)
                        raise
                else:
                    l=0
                max_len = max(max_len, l)
        return max_len*max_len
                
                    
                
