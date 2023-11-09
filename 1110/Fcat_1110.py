from collections import deque
from typing import List


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        queue = deque()

        result = []
        if root and root.val not in to_delete_set:
            result.append(root)
            queue.append((root, False))
        else:
            queue.append((root, True))
        while queue:
            node, is_deleted = queue.popleft()
            if node is None:
                continue

            if node.left and node.left.val not in to_delete_set:
                if is_deleted:
                    result.append(node.left)
                queue.append((node.left, False))
            else:
                queue.append((node.left, True))
                node.left = None

            if node.right and node.right.val not in to_delete_set:
                if is_deleted:
                    result.append(node.right)
                queue.append((node.right, False))
            else:
                queue.append((node.right, True))
                node.right = None
        return result