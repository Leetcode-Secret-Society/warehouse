# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        if root == None:
            return 0
        self.count = 0
        #Solution-1
        def dfs(root, start, s):
            if not root:
                return
            s -= root.val 
            if s==0:
                self.count+=1
            dfs(root.left,False, s)
            dfs(root.right,False, s)
            if start: #using every node as root..
                dfs(root.left,True,targetSum)
                dfs(root.right,True,targetSum)
        dfs(root,True,targetSum)
        return self.count

        #Solution-2
        def findLeaves(node: TreeNode, current_sums: list[int]):
            current_sums.append(node.val)
            temp_sum = 0
            for i in range(len(current_sums)):
                temp_sum += current_sums[-i - 1]
                if temp_sum == targetSum:
                    self.count += 1
            if node.left:
                findLeaves(node.left, list(current_sums))
            if node.right:
                findLeaves(node.right, list(current_sums))
        findLeaves(root, [])
        return self.count
