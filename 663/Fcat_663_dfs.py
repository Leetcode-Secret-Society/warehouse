# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        subtree_sum_list = []
        def get_subtree_sum(node):
            if not node:
                return 0
            left_sum = get_subtree_sum(node.left)
            right_sum = get_subtree_sum(node.right)

            subtree_sum_list.append(node.val + left_sum + right_sum)
            return subtree_sum_list[-1]
        total = get_subtree_sum(root)
        subtree_sum_list.pop()
        return (total / 2) in subtree_sum_list
