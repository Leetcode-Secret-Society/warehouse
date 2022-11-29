class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.deepestLevel = 0
        level_sum = [0]
        def dfs(node, level):
            if not node:
                return
            if level > self.deepestLevel:
                level_sum.append(0)
                self.deepestLevel += 1
            level_sum[level] += node.val
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 0)
        return level_sum[-1]