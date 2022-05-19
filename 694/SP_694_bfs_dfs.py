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
        def bfs(cur: Coordinate, boundary: Coordinate, grid: List[List[int]], direction): #some say it is dfs...
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
            path.append('0')
                
            
        R, C = len(grid), len(grid[0])
        
        count_set = set()
        for row in range(R):
            for col in range(C):
                path.clear()
                bfs(Coordinate(col,row), Coordinate(C,R), grid,"")
                if len(path) > 0:
                    count_set.add("".join(path))
        return len(count_set)
