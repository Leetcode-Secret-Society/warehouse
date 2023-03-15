# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left =left
        self.right = right
        self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None
        copied_root = NodeCopy(val=root.val)
        queue = [root]
        copy_queue = [copied_root]
        copied_node_pool = {id(root): copied_root} # original node id is key
        while queue:
            new_queue = []
            new_copy_queue = []
            for node, copied_node in zip(queue, copy_queue):
                if node.left:
                    new_queue.append(node.left)
                    if id(node.left) in copied_node_pool:
                        copied_left = copied_node_pool[id(node.left)]
                    else:
                        copied_left = NodeCopy(val=node.left.val)
                        copied_node_pool[id(node.left)] = copied_left
                    new_copy_queue.append(copied_left)
                    copied_node.left = copied_left
                if node.right:
                    new_queue.append(node.right)
                    if id(node.right) in copied_node_pool:
                        copied_right = copied_node_pool[id(node.right)]
                    else:
                        copied_right = NodeCopy(val=node.right.val)
                        copied_node_pool[id(node.right)] = copied_right
                    new_copy_queue.append(copied_right)
                    copied_node.right = copied_right
                if node.random:
                    if id(node.random) in copied_node_pool:
                        copied_random = copied_node_pool[id(node.random)]
                    else:
                        copied_random = NodeCopy(val=node.random.val)
                        copied_node_pool[id(node.random)] = copied_random
                    copied_node.random = copied_random
            queue = new_queue
            copy_queue = new_copy_queue
        return copied_root
