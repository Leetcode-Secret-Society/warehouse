from collections import deque

class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:

        queue = deque()
        queue.append([None, None, root])
        checked = set()
        checked.add(root.val)
        while queue:
            parent, direction, node = queue.popleft()
            if node.left:
                if node.left.val in checked:
                    setattr(parent, direction, None)
                    return root
                checked.add(node.left.val)
                queue.append([node, 'left', node.left])
            if node.right:
                if node.right.val in checked:
                    setattr(parent, direction, None)
                    return root
                checked.add(node.right.val)
                queue.append([node, 'right', node.right])
