class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        recorded_path = defaultdict(int)
        self.m = len(grid)
        self.n = len(grid[0])
        self.directions = [(1,0), (-1,0), (0, 1), (0, -1)]

        def check_all_blocked(grids: Tuple[Tuple[int]]):
            for j in range(self.m):
                for i in range(self.n):
                    if grids[j][i] == 0:
                        return False
            return True

        def check_pos_valid(grids: Tuple[Tuple[int]], pos: Tuple) -> bool:
            x = pos[0]
            y = pos[1]
            return x >= 0 and x < self.n and y >= 0 and y < self.m and grids[y][x]!=-1

        def cal_path(grids: Tuple[Tuple[int]], startPos: Tuple, endPos: Tuple) -> int:
            if grids in recorded_path:
                return recorded_path[grids]
            else:
                if startPos == endPos:
                    if check_all_blocked(grids):
                        recorded_path[grids] = 1
                        return 1
                    else:
                        recorded_path[grids] = 0
                        return 0
                
                path_count = 0
                for direction in self.directions:
                    nextStartPos = (startPos[0]+direction[0], startPos[1]+direction[1])
                    if not check_pos_valid(grids, nextStartPos):
                        continue
                    pos_cell_dict = {
                        nextStartPos: 1,
                        startPos: -1
                    }
                    nextGrid = tuple(tuple(pos_cell_dict[(x, y)] if (x, y) in pos_cell_dict else cell for x, cell in enumerate(row))  for y, row in enumerate(grids))
                    path_count += cal_path(nextGrid, nextStartPos, endPos)
                recorded_path[grids] = path_count
                return path_count
        
        gridTuple = tuple(tuple(cell for cell in row) for row in grid)
        for y in range(self.m):
            for x in range(self.n):
                if grid[y][x]==1:
                    startPos = (x, y)
                elif grid[y][x]==2:
                    endPos = (x, y)

        ans = cal_path(gridTuple, startPos, endPos)
        #print(recorded_path)

        return ans
