# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        path_set1 = set()
        path_set2 = set()
        def dfs_set(node, path, path_set):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right:
                path_set.add(tuple(path))
            else:
                if node.left:
                    dfs_set(node.left, path, path_set)
                if node.right:
                    dfs_set(node.right, path, path_set)
            path.pop()
        
        dfs_set(root1, [], path_set1)
        dfs_set(root2, [], path_set2)
        print(path_set1)
        print(path_set2)
        print(path_set1.difference(path_set2))

        return path_set1==path_set2
        
        
