# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        row_max_list = []
        while queue:
            new_queue = []
            row_max = float('-inf')
            for node in queue:
                row_max = max(node.val, row_max)
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            row_max_list.append(row_max)
            queue = new_queue
        return row_max_list
