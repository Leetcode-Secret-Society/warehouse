# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        the_highest_ancestor = float('inf')
        the_deepest = 0
        candidate_node = None
        
        def get_deepest(node, curr):
            nonlocal the_deepest
            if not node:
                the_deepest = max(the_deepest, curr)
                return
            get_deepest(node.left, curr+1)
            get_deepest(node.right, curr+1)
            
        get_deepest(root, 0)
        def get_depth(node, curr):
            nonlocal the_highest_ancestor
            nonlocal candidate_node
            if not node:
                return curr
            left_depth = get_depth(node.left, curr+1)
            right_depth = get_depth(node.right, curr+1)
            if left_depth == right_depth == the_deepest and curr < the_highest_ancestor:
                the_highest_ancestor = curr
                candidate_node = node
            return max(left_depth, right_depth)
        get_depth(root, 0)
        return candidate_node
