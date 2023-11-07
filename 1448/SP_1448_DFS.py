# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def findLeaves(node: TreeNode, current_max: int):
            if current_max <= node.val:
                self.count += 1
            if node.left:
                findLeaves(node.left, max(current_max, node.val))
            if node.right:
                findLeaves(node.right, max(current_max, node.val))

        findLeaves(root, root.val)
        return self.count
