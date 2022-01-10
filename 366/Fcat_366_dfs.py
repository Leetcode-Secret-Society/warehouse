# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.depth = 0
        def dfs_build_depth(node, depth):
            if not node:
                return depth - 1
            self.depth = max(self.depth, depth)
            left_depth = dfs_build_depth(node.left, depth + 1)
            right_depth = dfs_build_depth(node.right, depth + 1)
            node.depth = depth
            node.deepest = max(left_depth, right_depth)
            return node.deepest

        def dfs_build_result(node):
            if not node:
                return
            order = node.deepest- node.depth
            result[order].append(node.val)
            dfs_build_result(node.left)
            dfs_build_result(node.right)

        dfs_build_depth(root, 0)
        result = [[] for i in range(self.depth+1)]
        dfs_build_result(root)
        return result
