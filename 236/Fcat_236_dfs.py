from typing import List


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def dfs(node):
            if self.ans is not None:
                return True

            if node is None:
                return False

            left_result = dfs(node.left)
            right_result = dfs(node.right)
            if self.ans is not None:
                return True
            if node == p or node == q:
                if left_result is True or right_result is True:
                    self.ans = node
                return True
            if left_result is True and right_result is True:
                self.ans = node
                return True

            return bool(left_result or right_result)

        dfs(root)
        return self.ans
