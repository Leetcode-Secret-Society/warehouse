class Node:
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.v = v
        self.out_nodes = []
        self.in_nodes = []
        self.min_step = None

class Solution:
    def get_neighbors(self, x, y):
        neighbors=[]
        if x-1>=0:
            neighbors.append(self.node_matrix[y][x-1])
        if x+1<self.width:
            neighbors.append(self.node_matrix[y][x+1])
        if y-1>=0:
            neighbors.append(self.node_matrix[y-1][x])
        if y+1<self.height:
            neighbors.append(self.node_matrix[y+1][x])
        return neighbors
    
    def dfs(self,node):
        if node.min_step:
            return node.min_step
        else:
            max_out_step = 0
            for out_node in node.out_nodes:
                out_step = self.dfs(out_node)
                max_out_step = max(max_out_step, out_step)
            node.min_step=max_out_step+1
            return max_out_step+1
        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.height = len(matrix)
        self.width = len(matrix[0])
        self.node_matrix=[[Node(x,y,matrix[y][x]) for x in range(self.width)] for y in range(self.height)]
        start_nodes = []
        for y in range(self.height):
            for x in range(self.width):
                current_node = self.node_matrix[y][x]
                neighbors=self.get_neighbors(x, y)
                for neighbor_node in neighbors:
                    if neighbor_node.v>current_node.v:
                        current_node.out_nodes.append(neighbor_node)
                    elif neighbor_node.v<current_node.v:
                        current_node.in_nodes.append(neighbor_node)
                if len(current_node.in_nodes) == 0:
                    start_nodes.append(current_node)
        max_length=1
        for start_node in start_nodes:
            length=self.dfs(start_node)
            max_length=max(max_length, length)
        return max_length
