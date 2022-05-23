class Coordinate:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"x={self.x}, y={self.y}"
    def __repr__(self):
        return f"x={self.x}, y={self.y}"
    

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        visited = set()
        path = list()
        def bfs(cur: Coordinate, boundary: Coordinate, grid: List[List[int]], direction):
            if (cur.x,cur.y) in visited:
                return
            if grid[cur.y][cur.x] == 0:
                return
            
            path.append(direction)
            visited.add((cur.x, cur.y))
            # print(cur)
            if cur.x + 1 < boundary.x:
                bfs(Coordinate(cur.x+1 , cur.y), boundary, grid, "R")
            if cur.x - 1 >= 0:
                bfs(Coordinate(cur.x-1 , cur.y), boundary, grid, "L")
            if cur.y + 1 < boundary.y:
                bfs(Coordinate(cur.x, cur.y + 1), boundary, grid, "D")
            if cur.y - 1 >= 0:
                bfs(Coordinate(cur.x, cur.y - 1), boundary, grid, "U")
            path.append('0') #append 0 to create signature path
            """
                [[1,1,1],[0,0,1],[0,0,0],[1,1,1],[0,1,0],[0,0,0],[1,1,1],[1,0,0],[0,0,0]]
                ans: 3
                but path is RRD if without 0 signature
                [[1,0],[1,1],[1,0],[0,0],[1,1],[1,0],[1,0],[0,0],[1,0],[1,0],[1,1],[0,0]]
                ans: 3
                path would be DRD,DDR,RDD but if search y first, it will be DDR
            """
                
            
        R, C = len(grid), len(grid[0])
        
        count_set = set()
        for row in range(R):
            for col in range(C):
                path.clear()
                bfs(Coordinate(col,row), Coordinate(C,R), grid,"")
                if len(path) > 0:
                    count_set.add("".join(path))
        print(f"{path=}, {count_set=}")
        return len(count_set)
