# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def dfs(node, length, last):
            if not node:
                return length
            if last == 'l':
                return max(dfs(node.right, length + 1, 'r'), dfs(node.left, 0, 'l'))
            else:
                return max(dfs(node.left, length + 1, 'l'), dfs(node.right, 0, 'r'))


        return max(dfs(root, -1, 'l'), dfs(root, -1, 'r'))
