# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def convert(p):
            return "*" + str(p.val) + "->[" + convert(p.left) + "-" + convert(p.right) + ']' if p else "Null"    
        r = convert(root)
        s = convert(subRoot)
        # print(f"{r=} {s=}")
        return s in r
