from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if node.right is None:
            parent_node = node.parent
            while parent_node:
                if parent_node.val > node.val:
                    return parent_node
                parent_node = parent_node.parent
            return None
        else:
            next_node = node.right

            while next_node.left:
                next_node = next_node.left
            return next_node
