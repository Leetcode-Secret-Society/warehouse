"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        length_of_grid = len(grid)
        node_grid = [[Node(e, True, None, None, None, None)for e in row] for row in grid]
        while len(node_grid)!=1:
            # narrow-down
            length_of_grid=len(node_grid)
            new_grid = []
            for y in range(0, length_of_grid-1, 2):
                row = []
                for x in range(0, length_of_grid-1, 2):
                    topLeftNode = node_grid[y][x]
                    bottomLeftNode = node_grid[y+1][x]
                    topRightNode = node_grid[y][x+1]
                    bottomRightNode = node_grid[y+1][x+1]
                    if topLeftNode.val == bottomLeftNode.val and bottomLeftNode.val == topRightNode.val and topRightNode.val == bottomRightNode.val and bottomRightNode.val in [0,1]:
                        row.append(Node(topLeftNode.val, True, None, None, None, None))
                    else:
                        row.append(Node(2, False, topLeftNode, topRightNode, bottomLeftNode, bottomRightNode))
                new_grid.append(row)
            node_grid = new_grid
        return node_grid[0][0]
        
                