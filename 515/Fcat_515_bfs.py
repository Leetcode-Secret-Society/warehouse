from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque()
        queue.append([0, root])

        while queue:
            level, node = queue.popleft()
            if node is None:
                continue
            if len(result) == level:
                result.append(node.val)
            else:
                result[level] = max(result[level], node.val)
            queue.append([level+1, node.left])
            queue.append([level+1, node.right])
        return result