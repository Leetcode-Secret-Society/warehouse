from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        examined_queue = [[root]]
        odd = True
        while examined_queue:
            next_queue = []
            current_queue = examined_queue.pop()
            last_val = None
            for node in current_queue:
                if not node:
                    continue
                if odd:
                    if node.val % 2 == 0:
                        return False
                    if last_val and node.val <= last_val:
                        return False
                else:
                    if node.val % 2 == 1:
                        return False
                    if last_val and node.val >= last_val:
                        return False

                last_val = node.val
                next_queue.append(node.left)
                next_queue.append(node.right)
            odd = not odd
            if next_queue:
                examined_queue.append(next_queue)

        return True
