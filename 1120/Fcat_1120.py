from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.result = 0.0

        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            if node is None:
                return 0, 0

            left_sum, left_node_num = dfs(node.left)
            right_sum, right_node_num = dfs(node.right)

            cur_sum = node.val + left_sum + right_sum
            cur_node_num = left_node_num + right_node_num + 1

            self.result = max(self.result, cur_sum / cur_node_num)
            return cur_sum, cur_node_num

        dfs(root)

        return self.result
