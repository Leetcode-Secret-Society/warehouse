# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def subtree_sum_check(node) -> (int, int):
            if not node:
                return 0, 0
            else:
                left_count, left_sum = subtree_sum_check(node.left)
                right_count, right_sum = subtree_sum_check(node.right)
                if node.val == (node.val+left_sum+right_sum)//(left_count+right_count+1):
                    self.count+=1
                return (left_count+right_count+1, left_sum+right_sum+node.val)
        subtree_sum_check(root)        
        return self.count
