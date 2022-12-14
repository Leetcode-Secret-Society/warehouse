# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            if node.val == x:
                self.lsubtree = dfs(node.left)
                self.rsubtree = dfs(node.right)
                return self.lsubtree+self.rsubtree + 1
            else:
                lsubtree = dfs(node.left)
                rsubtree = dfs(node.right)
                return lsubtree + rsubtree + 1
        total = dfs(root)
        parent_tree = total - self.lsubtree - self.rsubtree - 1
        tree_node_counts = [parent_tree, self.lsubtree, self.rsubtree]
        tree_node_counts.sort()
        
        return tree_node_counts[2] > tree_node_counts[1] + 1 + tree_node_counts[0]
            
