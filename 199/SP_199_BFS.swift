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
    func rightSideView(_ root: TreeNode?) -> [Int] {
        var stack = [root]
        var nextStack = [TreeNode]()
        var result = [Int]()
        
        while stack.count > 0, let node = stack.removeFirst() {
            // print(node.val)
            if let left = node.left {
                nextStack.append(left)
            }
            if let right = node.right {
                nextStack.append(right)
            }
            if stack.count == 0 {
                result.append(node.val)
                stack = Array(nextStack)
                nextStack.removeAll()
            }
        }
        
        return result
    }
}
