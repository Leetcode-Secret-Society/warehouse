# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        if not root:
            # print("None")
            return None
        # print(root.val)
        if root in nodes:
            # print("ancestor-self-"+str(root.val))
            return root
        left = self.lowestCommonAncestor(root.left, nodes)
        right = self.lowestCommonAncestor(root.right, nodes)

        if left in nodes and right in nodes:
            # print("ancestor-"+str(root.val)+" l:"+str(left.val)+" r:"+str(right.val))
            return root
        if left:
            # print("left-"+str(root.val)+"-"+str(left.val))
            return left
        if right:
            # print("right-"+str(root.val)+"-"+str(right.val))
            return right
        # print("None-END-"+str(root.val))
        return None
