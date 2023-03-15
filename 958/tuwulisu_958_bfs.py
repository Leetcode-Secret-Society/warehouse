# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        continueous = True
        while queue:
            new_queue = []
            for n in queue:
                if n.left:
                    if not continueous:
                        return False
                    new_queue.append(n.left)
                else:
                    continueous = False
                if n.right:
                    if not continueous:
                        return False
                    new_queue.append(n.right)
                else:
                    continueous = False
            queue = new_queue
        return True
