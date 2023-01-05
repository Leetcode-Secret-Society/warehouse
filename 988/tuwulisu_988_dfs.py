# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.min_str = "zzzzzzzzzzzzzzzzzzzzzzz"
        def dfs(node, current_str_list):
            if not node:
                return
            if not node.left and not node.right:
                self.min_str = min(self.min_str, "".join([chr(node.val+97)]+current_str_list))
                return
            dfs(node.left, [chr(node.val+97)]+current_str_list)
            dfs(node.right, [chr(node.val+97)]+current_str_list)
        dfs(root, [])
        return self.min_str
            
