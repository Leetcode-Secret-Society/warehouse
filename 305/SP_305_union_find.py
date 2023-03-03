class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # from 200. Number of Islands, some differences are commented.
        width, height = m, n
        self.count = 0
        parent = {}
        seen = set()
        result = []
        
        # for x in range(width):
        #     for y in range(height):
        #         if grid[x][y] == "1":
        #             self.count += 1
        #             parent[(x,y)] = (x,y)
        
        def find(pos):
            if pos in parent:
                if parent[pos] != pos:
                    parent[pos] = find(parent[pos])
            else:
                parent[pos] = pos
            return parent[pos]
        def union(a,b):
            a_parent, b_parent = find(a), find(b)
            if a_parent != b_parent: 
                parent[b_parent] = a_parent
                self.count -= 1

        # for x,y in parent.keys():
        #     if x+1 < width and grid[x+1][y] == "1":
        #         union((x,y),(x+1,y))
        #     if y+1 < height and grid[x][y+1] == "1":
        #         union((x,y),(x,y+1))

        for x,y in positions:
            if (x,y) not in seen:
                seen.add((x,y))
                self.count+=1
                for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if (i,j) in seen:
                        union((i,j),(x,y))
            result.append(self.count)
        return result
