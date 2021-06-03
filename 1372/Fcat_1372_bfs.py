# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        max_len = 0
        bfs_list = [(root, -1, 'l'), (root, -1, 'r')]

        for node, length, last in bfs_list:
            if node is None:
                max_len = max(max_len, length)
                continue
            if last == 'l':
                bfs_list.append((node.right, length + 1, 'r'))
                bfs_list.append((node.left, 0, 'l'))
            elif last == 'r':
                bfs_list.append((node.left, length + 1, 'l'))
                bfs_list.append((node.right, 0, 'r'))
        return max_len
