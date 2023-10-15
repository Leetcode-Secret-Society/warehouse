from typing import List, Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        queue = deque()
        queue.append([root, 0])
        while queue:
            node, level = queue.popleft()
            if node is None:
                continue
            if len(result) == level:
                result.append(node.val)

            queue.append([node.right, level + 1])
            queue.append([node.left, level + 1])

        return result

