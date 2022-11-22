# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.movement = 0
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.calculate_movement(root)
        return self.movement
    def calculate_movement(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            l_movement = self.calculate_movement(root.left)
            r_movement = self.calculate_movement(root.right)
            root.val = root.val + l_movement + r_movement
            node_movement = root.val - 1
            self.movement += abs(node_movement)
            return node_movement
        
