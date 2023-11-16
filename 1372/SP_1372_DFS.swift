/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
    func longestZigZag(_ root: TreeNode?) -> Int {
        var maxDepth = 0
        func dfs(_ node: TreeNode?,_ goLeft: Bool,_ step: Int) {
            guard let node = node else {return}
            
            maxDepth = max(step, maxDepth)
            if goLeft {
                dfs(node.right, false, step + 1)
                dfs(node.left, true, 1)
            }
            else {
                dfs(node.right, false, 1)
                dfs(node.left, true, step + 1)
            }
        }

        dfs(root, false, 0)
        dfs(root, true, 0)

        return maxDepth
    }
}
