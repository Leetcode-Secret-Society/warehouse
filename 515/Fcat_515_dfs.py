from typing import Optional, List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(level, node):
            if node is None:
                return
            if len(result) == level:
                result.append(node.val)
            else:
                result[level] = max(result[level], node.val)
            dfs(level + 1, node.left)
            dfs(level + 1, node.right)

        dfs(0, root)

        return result