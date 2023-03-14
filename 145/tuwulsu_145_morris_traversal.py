# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def reverse_order(node):
            prev = None
            while node:
                next_node = node.right
                node.right = prev
                prev = node
                node = next_node
            return prev
        dummy = TreeNode(0)
        dummy.left = root
        root = dummy
        ans = []
        while root:
            if not root.left:
                root = root.right
            else:
                right_most = root.left
                while right_most.right and right_most.right != root:
                    right_most = right_most.right
                if not right_most.right:
                    right_most.right = root
                    root = root.left
                else:
                    right_most.right = None
                    leaf = reverse_order(root.left)
                    reverse_pointer = leaf
                    while reverse_pointer:
                        ans.append(reverse_pointer.val)
                        reverse_pointer = reverse_pointer.right
                    reverse_order(leaf)
                    root = root.right
        return ans
