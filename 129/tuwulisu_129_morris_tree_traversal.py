# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum_of_tree = 0
        sum_of_path = 0
        dummy = TreeNode(0)
        dummy.left = root
        root = dummy
        while root:
            if root.left:
                right_most_node = root.left
                depth = 1
                while right_most_node.right and right_most_node.right is not root:
                    right_most_node = right_most_node.right
                    depth+=1
                if not right_most_node.right:
                    sum_of_path *= 10
                    sum_of_path += root.val
                    right_most_node.right = root
                    root = root.left
                else:
                    right_most_node.right = None
                    if not right_most_node.left and not right_most_node.right:
                        sum_of_tree+=sum_of_path
                    sum_of_path//=10**depth
                    root = root.right
            else:
                sum_of_path *= 10
                sum_of_path += root.val
                root = root.right
        sum_of_tree+=sum_of_path
        return sum_of_tree
