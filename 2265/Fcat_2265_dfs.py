# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node): #sub_node_count, sub_node_sum, condition_satisfied_count
            if node is None:
                return 0, 0, 0
            left_node_count, left_node_sum, left_result = dfs(node.left)
            right_node_count, right_node_sum, right_result =dfs(node.right)
            cur_sum = node.val + left_node_sum + right_node_sum
            cur_node_count = 1 + left_node_count + right_node_count
            is_equal_avg = 1 if cur_sum // cur_node_count == node.val else 0

            return cur_node_count, cur_sum, left_result + right_result + is_equal_avg
        _,_, result = dfs(root)
        return result


