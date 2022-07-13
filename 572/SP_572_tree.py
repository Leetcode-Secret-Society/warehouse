# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMatch(source, target) -> bool:
        if source == None or target == None:
            return source == target #return True if both None
        if source.val == target.val:
            return Solution.isMatch(source.left, target.left) and Solution.isMatch(source.right, target.right)
        return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if Solution.isMatch(root, subRoot):
            return True
        if root == None:
            return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
