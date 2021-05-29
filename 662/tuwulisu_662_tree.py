# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue=[[root,0]]
        max_width=1
        while queue:
            new_queue=[]
            for node,node_id in queue:
                if node.left:
                    new_queue.append([node.left,node_id*2])
                if node.right:
                    new_queue.append([node.right,node_id*2+1])
            if len(new_queue)>=2:
                max_width=max(max_width,new_queue[-1][1] - new_queue[0][1] + 1)
            queue=new_queue
        return max_width
