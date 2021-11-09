

class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre_order_list = []

        def dfs(node):
            if not node:
                return
            pre_order_list.append(node)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        for i in range(len(pre_order_list)-1):
            node = pre_order_list[i]
            node.left = None
            node.right = pre_order_list[i+1]

        if pre_order_list:
            pre_order_list[-1].left = None
            pre_order_list[-1].right = None
        return root