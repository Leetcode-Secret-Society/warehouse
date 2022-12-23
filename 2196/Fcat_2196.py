from typing import List
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        for parent, child, is_left in descriptions:
            if child not in nodes:
                nodes[child] = TreeNode(child)
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

        nodes_set = set(nodes.keys())
        for _, child, _ in descriptions:
            nodes_set.remove(child)
        root = list(nodes_set)[0]
        return nodes[root]
