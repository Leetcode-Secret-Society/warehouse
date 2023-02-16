class Node:
    def __init__(self, y, x, cell):
        self.y = y
        self.x = x
        self.cell = cell
        self.head = self
        self.count = 1
    def find_head(self):
        curr = self
        middles = []
        while curr.head is not curr:
            middles.append(curr)
            curr = curr.head
        for middle in middles:
            middle.head = curr
        return curr
    def join(self, node):
        node.head = self
        node.count+=self.count
    def flip(self):
        assert self.cell == 0
        self.cell = 1
    def __hash__(self):
        return id(self)
    def __repr__(self):
        return f"[{self.y=}, {self.x=}, {self.cell=}]"
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        union_find_map = [[Node(y, x, 0) for x in range(n)] for y in range(m)]
        lands = 0
        ans = []
        for i, position in enumerate(positions):
            y=position[0]
            x=position[1]

            if union_find_map[y][x].cell == 1:
                ans.append(lands)
                continue
            else:
                adj_lands = set()
                for adj_y, adj_x in [(y+1,x), (y-1,x), (y, x+1), (y, x-1)]:
                    if adj_y>=0 and adj_y<m and adj_x>=0 and adj_x<n and union_find_map[adj_y][adj_x].cell==1:
                        adj_head = union_find_map[adj_y][adj_x].find_head()
                        if adj_head not in adj_lands:
                            adj_lands.add(adj_head)
                if adj_lands:
                    lands-= len(adj_lands)-1
                    adj_lands = list(adj_lands)
                    adj_lands.sort(key=lambda n: n.count, reverse=True)
                    adj_lands[0].join(union_find_map[y][x])
                    for small_land in adj_lands[1:]:
                        adj_lands[0].join(small_land)
                else:
                    lands+=1
                union_find_map[y][x].flip()
            ans.append(lands)
        return ans
                    
        
