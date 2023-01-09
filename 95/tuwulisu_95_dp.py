# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        tree_memo = {
            (1, 1): [TreeNode(1)]
        }
        def duplicate_tree_with_bias(tree_root, bias):
            if tree_root is None:
                return None
            new_root = TreeNode(tree_root.val+bias)
            new_root.left = duplicate_tree_with_bias(tree_root.left, bias)
            new_root.right = duplicate_tree_with_bias(tree_root.right, bias)
            return new_root
        def generate_subtree(n, root_val):
            #print(n, root_val)
            if n==0:
                return [None]
            if n==1:
                return [TreeNode(root_val)]
            if (n, root_val) in tree_memo:
                return tree_memo[(n, root_val)]
            bias = root_val - 1
            variants = tree_memo[(n, 1)]
            if bias == 0:
                return variants
            subtrees = []
            for tree_root in variants:
                new_root = duplicate_tree_with_bias(tree_root, bias)
                subtrees.append(new_root)
            tree_memo[(n, root_val)] = subtrees
            return subtrees

        for i in range(2,n+1):
            ans_on_i = []
            for root_val in range(1,i+1):
                left_trees = generate_subtree(root_val-1, 1)
                right_trees = generate_subtree(i-root_val, root_val+1)
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(val=root_val)
                        root.left = left_tree
                        root.right = right_tree
                        ans_on_i.append(root)
            #print(f"set ({i}, 1)")
            tree_memo[(i, 1)] = ans_on_i
        #print(tree_memo)
        return tree_memo[(n, 1)]
                
