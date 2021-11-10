class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur_node = root

        while cur_node:

            if cur_node.left:
                next_node = cur_node.left
                while next_node.right:
                    next_node = next_node.right
                next_node.right = cur_node.right

                cur_node.right = cur_node.left
                cur_node.left = None

            cur_node = cur_node.right


        return root