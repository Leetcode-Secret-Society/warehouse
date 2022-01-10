# Definition for a binary tree node.
from typing import List
from collections import defaultdict, deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root) -> List[List[int]]:
        if not root: return []
        position_mapping = defaultdict(list)
        bound = [0,0]
        bfs = deque([(root, 0)])
        while bfs:
            node, pos = bfs.popleft()
            position_mapping[pos].append(node.val)
            if node.left:
                bound[0] = min(bound[0], pos - 1)
                bfs.append((node.left, pos - 1))
            if node.right:
                bound[1] = max(bound[1], pos + 1)
                bfs.append((node.right, pos + 1))

        result = []
        for i in range(bound[0], bound[1]+1):
            result.append(position_mapping[i])
        return result

