# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        self.equal_count = 0
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            descendant_sum = left_sum + right_sum
            if node.val == descendant_sum:
                self.equal_count += 1
            return descendant_sum + node.val
        dfs(root)
        return self.equal_count