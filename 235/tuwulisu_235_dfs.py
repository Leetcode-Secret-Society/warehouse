# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        CA = []
        def dfs(node: 'TreeNode') -> set:
            if not node:
                return set()
            left_set = dfs(node.left)
            right_set = dfs(node.right)
            final_set = left_set.union(right_set)
            final_set.add(node.val)
            if p.val in final_set and q.val in final_set:
                CA.append(node)
            return final_set
        dfs(root)
        return CA[0]
