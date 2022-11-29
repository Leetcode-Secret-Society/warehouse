class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = [(root, 0)]
        for node,level in queue:
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        total = 0
        deepest_level = queue[-1][1]
        for i in range(len(queue)-1, -1 , -1):
            node, level = queue[i]
            if level != deepest_level:
                break
            total += node.val

        return total