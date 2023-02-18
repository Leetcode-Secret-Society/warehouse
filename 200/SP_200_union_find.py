class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        width, height = len(grid), len(grid[0])
        self.count = 0
        parent = defaultdict()
        for x in range(width):
            for y in range(height):
                if grid[x][y] == "1":
                    self.count += 1
                    parent[(x,y)] = (x,y)
        def find(pos):
            if parent[pos] != pos:
                parent[pos] = find(parent[pos])
            return parent[pos]
        def union(a,b):
            a_parent, b_parent = find(a), find(b)
            if a_parent != b_parent: 
                parent[b_parent] = a_parent
                self.count -= 1

        for x,y in parent.keys():
            if x+1 < width and grid[x+1][y] == "1":
                union((x,y),(x+1,y))
            if y+1 < height and grid[x][y+1] == "1":
                union((x,y),(x,y+1))
        return self.count
