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
    func findLeaves(_ root: TreeNode?) -> [[Int]] {
        var resultDic = [Int:[Int]]()
        func getHeight(_ node: TreeNode?) -> Int{
            guard let node = node else {return 0} 
            let height = max(getHeight(node.left), getHeight(node.right)) + 1
            if resultDic[height] == nil {
                resultDic[height] = [node.val]
            } else {
                resultDic[height]?.append(node.val)
            }
            return height
        }
        getHeight(root)
        var result = [[Int]]()
        for height in resultDic.keys.sorted() {
            if let roots = resultDic[height] {
                result.append(roots)
            }
        }
        return result
    }
}
